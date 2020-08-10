class Action:
    def act(self, message, *args, **kwargs):
        ...

    @property
    def tbot(self):
        from chaban.bots import TelegramBot

        return TelegramBot()
