from chaban.actions.action import Action


class StartCommandAction(Action):
    def act(self, message):
        print(message)
