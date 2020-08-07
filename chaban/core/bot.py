import typing

import httpx

from .exceptions import HttpMethodNotAllowed
from .tg_methods import TelegramMethodsMixin


class Bot(TelegramMethodsMixin):
    _allowed_http_methods = ["get", "post"]

    def __init__(self, token: str):
        if not isinstance(token, str):
            raise TypeError(":param token: must a be string")

        self._endpoint = "https://api.telegram.org/bot{}/".format(token)

    def _build_url(self, method_name: str) -> str:
        return self._endpoint + method_name.lstrip("/")

    def request(
        self, method_name: str, http_method: str = "get", **kwargs
    ) -> typing.Dict[str, typing.Any]:
        if http_method not in self._allowed_http_methods:
            raise HttpMethodNotAllowed

        return httpx.request(
            http_method, self._build_url(method_name), params=kwargs
        ).json()
