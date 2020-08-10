from chaban import Action


class StartCommandAction(Action):
    def act(self, message):
        self.tbot.send_message(message["chat"]["id"], message["text"] + "!")
