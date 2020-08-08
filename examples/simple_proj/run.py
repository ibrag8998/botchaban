import sys
from pathlib import Path


def run():
    root_path = Path(__file__).parent
    sys.path.append(root_path / "simple_proj")


if __name__ == "__main__":
    run()
