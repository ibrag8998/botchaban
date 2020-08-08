import environs

from chaban.core.bot import Bot
from chaban.handlers.specials import CommandMH

env = environs.Env()
env.read_env()

bot = Bot(env("TOKEN"))
admin_id = env.int("ADMIN_ID")

# === #


def respond(message):
    print(1)


class StartCommandMH(CommandMH):
    command = "start"

    action = respond


bot.start_polling()
