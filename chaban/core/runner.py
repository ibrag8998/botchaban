import sys
import typing as typ
from pathlib import Path

from chaban.config import settings
from chaban.utils import SingletonMixin


class _Runner(SingletonMixin):
    """
    Runner class to run your application

    The only public method is ``run``, so you know what to do :)
    """

    def run(self, client_run_file: typ.Union[Path, str]):
        # make it Path
        client_run_file = Path(client_run_file)

        # do all the job related to settings.PACKAGES
        self._handle_packages(client_run_file.parent)

    def _handle_packages(self, client_root_path: Path) -> None:
        # get package list from settings
        pkgs = settings.PACKAGES[:]
        for pkg_name in pkgs:
            # get each package path in str format
            pkg_path = str(client_root_path / pkg_name)
            # append each package to sys.path
            sys.path.append(pkg_path)
            # plain import each package to handle message handlers, actions, etc
            pkg = __import__(pkg_path)
            print(dir(pkg))
            print(pkg.__path__)
            print(pkg.__package__)


runner = _Runner()
