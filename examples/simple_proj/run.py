import os
import sys
from pathlib import Path

from chaban.core.telegram_bot import TelegramBot


def run():
    os.environ["CHABAN_SETTINGS_MODULE"] = "settings"

    root_path = Path(__file__).parent
    sys.path.append(root_path / "simple_proj")

    # debugging purposes ...
    tbot = TelegramBot()

    tbot.start_polling()


if __name__ == "__main__":
    run()
