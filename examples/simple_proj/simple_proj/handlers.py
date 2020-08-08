from chaban.handlers.specials import CommandMH

from .actions import StartCommandAction


class StartCommandMH(CommandMH):
    command = "start"
    action = StartCommandAction
