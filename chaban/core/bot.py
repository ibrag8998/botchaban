import typing

import httpx

from chaban.config import settings
from chaban.utils import SingletonMixin

from .exceptions import HttpMethodNotAllowed, TelegramAPIError
from .tg_methods import TelegramMethodsMixin


class Bot(TelegramMethodsMixin, SingletonMixin):
    _allowed_http_methods = ["get", "post"]

    def __init__(self):
        self._endpoint = "https://api.telegram.org/bot{}/".format(settings.TOKEN)

    def _build_url(self, method_name: str) -> str:
        return self._endpoint + method_name.lstrip("/")

    def request(
        self, method_name: str, http_method: str = "get", **kwargs
    ) -> typing.Dict[str, typing.Any]:
        if http_method.lower() not in self._allowed_http_methods:
            raise HttpMethodNotAllowed

        return httpx.request(
            http_method, self._build_url(method_name), params=kwargs
        ).json()

    def start_polling(self):
        offset = 0

        while True:
            resp = self.get_updates(offset=offset)

            if not resp["ok"]:
                raise TelegramAPIError("Response JSON: {}".format(resp))

            print(resp)
