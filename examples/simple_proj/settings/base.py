from pathlib import Path

from environs import Env

BASE_DIR = Path(__file__).parent.parent

env = Env()
env.read_env()

TOKEN = env("TOKEN")
if TOKEN is None:
    raise EnvironmentError("TOKEN env variable is required, but not set")

ADMIN_ID = env.int("ADMIN_ID")
