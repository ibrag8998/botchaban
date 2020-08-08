import typing as typ


class TelegramMethodsMixin:
    # For IDE support, define a request method without defining its body
    def request(
        self, method_name: str, http_method: str = "get", **kwargs
    ) -> typ.Dict[str, typ.Any]:
        ...

    # ==== ==== ==== ==== ==== #
    # === Telegram methods === #
    # ==== ==== ==== ==== ==== #

    def get_me(self, **kwargs):
        return self.request("getMe", **kwargs)

    def send_message(self, chat_id: typ.Union[int, str], text: str, **kwargs):
        return self.request("sendMessage", chat_id=chat_id, text=text)

    def get_updates(self, offset: typ.Optional[int] = None, **kwargs):
        return self.request("getUpdates", offset=offset, **kwargs)
