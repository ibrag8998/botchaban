from pathlib import Path

from environs import Env

BASE_DIR = Path(__file__).parent.parent

env = Env()
env.read_env()

TELEGRAM_TOKEN = env("TELEGRAM_TOKEN")
if TELEGRAM_TOKEN is None:
    raise EnvironmentError("TELEGRAM_TOKEN env variable is required, but not set")

PACKAGES = [
    "simple_proj",
]

ADMIN_ID = env.int("ADMIN_ID")
