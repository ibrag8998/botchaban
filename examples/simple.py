import environs

from chaban.core.bot import Bot

env = environs.Env()
env.read_env()

bot = Bot(env("TOKEN"))

print(bot.request("getMe"))
