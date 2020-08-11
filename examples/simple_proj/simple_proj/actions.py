from chaban import Action

from . import text


class StartCommandAction(Action):
    def act(self, message):
        self.tbot.send_message(message["chat"]["id"], text.START_COMMAND)
