import environs

from chaban.core.bot import Bot
from chaban.handlers.specials import CommandMH

env = environs.Env()
env.read_env()

bot = Bot(env("TOKEN"))
admin_id = env.int("ADMIN_ID")

# === #


class StartCommandMH(CommandMH):
    command = "start"


bot.start_polling()
