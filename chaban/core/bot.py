import typing

import httpx

from .exceptions import HttpMethodNotAllowed


class Bot:
    _allowed_http_meths = ["get", "post"]

    def __init__(self, token: str):
        if not isinstance(token, str):
            raise TypeError(":param token: must a be string")

        self._endpoint = "https://api.telegram.org/bot{}/".format(token)

    def _build_url(self, meth_name: str) -> str:
        return self._endpoint + meth_name.lstrip("/")

    def request(
        self, meth_name: str, http_meth: str = "get", **kwargs
    ) -> typing.Dict[str, typing.Any]:
        if http_meth not in self._allowed_http_meths:
            raise HttpMethodNotAllowed

        return httpx.request(
            http_meth, self._build_url(meth_name), params=kwargs
        ).json()
