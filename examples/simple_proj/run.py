import os
import sys
from pathlib import Path

from chaban.core.bot import Bot


def run():
    os.environ["CHABAN_SETTINGS_MODULE"] = "settings"

    root_path = Path(__file__).parent
    sys.path.append(root_path / "simple_proj")

    print(Bot()._endpoint)


if __name__ == "__main__":
    run()
