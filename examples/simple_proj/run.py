import os

from chaban.bots import TelegramBot
from chaban.core.runner import runner


def run():
    os.environ["CHABAN_SETTINGS_MODULE"] = "settings"

    runner.run(__file__)

    tbot = TelegramBot()
    tbot.start_polling()


if __name__ == "__main__":
    run()
