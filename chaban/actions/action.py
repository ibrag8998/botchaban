import typing as typ


class Action:
    def act(self, message: typ.Dict[str, typ.Any]):
        ...

    @property
    def tbot(self):
        from chaban.bots import TelegramBot  # TODO

        return TelegramBot()
