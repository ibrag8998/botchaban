from chaban.actions import Action


class StartCommandAction(Action):
    def act(self, message):
        print(message)
