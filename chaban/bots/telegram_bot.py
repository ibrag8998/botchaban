import typing as typ

import httpx

from chaban.config import global_settings, settings
from chaban.core.exceptions import HttpMethodNotAllowed, TelegramAPIError
from chaban.handlers.base import mh_registry
from chaban.utils import SingletonMixin

from .telegram_methods import TelegramMethodsMixin


class TelegramBot(TelegramMethodsMixin, SingletonMixin):
    """
    Main telegram bot class.

    All methods related to telegram api are defined in ``TelegramMethodsMixin``.

    On init, get ``TELEGRAM_TOKEN`` from settings.
    Settings are getting that token from env.
    """

    _allowed_http_methods = global_settings.TELEGRAM_ALLOWED_HTTP_METHODS

    def __init__(self):
        # bot don't need the token as a separate constant, token is only used as part of
        # the telegram api endpoint url
        self._endpoint = "https://api.telegram.org/bot{}/".format(
            settings.TELEGRAM_TOKEN
        )

    def _build_url(self, method_name: str) -> str:
        return self._endpoint + method_name.lstrip("/")

    def request(
        self, method_name: str, http_method: str = "get", **kwargs
    ) -> typ.Dict[str, typ.Any]:
        """
        Perform an HTTP :param http_method: request and pass the kwargs as params.

        Returns a JSON.
        """
        http_method = http_method.lower()

        if http_method not in self._allowed_http_methods:
            raise HttpMethodNotAllowed

        return httpx.request(
            http_method, self._build_url(method_name), params=kwargs
        ).json()

    def start_polling(self):
        for message in self._poll_updates():
            mh_registry.get_handler_and_handle(message)

    def _poll_updates(self) -> typ.Iterator[typ.Dict[str, typ.Any]]:
        """
        Main loop.

        Getting updates from telegram, handling offset, yielding each update's message
        """
        # set offset to 0
        offset = 0

        # start loop
        while True:
            # get json response from telegram
            resp = self.get_updates(offset=offset)

            # if not ok, raise the error
            if not resp["ok"]:
                raise TelegramAPIError("Response JSON: {}".format(resp))

            # iterate through updates from resp json
            for update in resp["result"]:
                # update offset
                offset = max(offset, update["update_id"] + 1)
                # yield message
                yield update.get("message", update.get("edited_message"))
