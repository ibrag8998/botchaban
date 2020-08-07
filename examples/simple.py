import environs

from chaban.core.bot import Bot

env = environs.Env()
env.read_env()

bot = Bot(env("TOKEN"))
admin_id = env.int("ADMIN_ID")

# === #
