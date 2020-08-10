from chaban import Action


class StartCommandAction(Action):
    @classmethod
    def act(cls, message):
        print(message)
