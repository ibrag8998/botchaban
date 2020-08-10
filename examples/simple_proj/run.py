import os

from chaban.core.runner import runner


def run():
    os.environ["CHABAN_SETTINGS_MODULE"] = "settings"

    runner.run(__file__)


if __name__ == "__main__":
    run()
