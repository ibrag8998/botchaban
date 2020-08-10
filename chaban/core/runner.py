import pkgutil
import sys
import typing as typ
from pathlib import Path

from chaban.bots import TelegramBot
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

        # start telegram bot
        self._start_telegram_bot()

    @staticmethod
    def _start_telegram_bot():
        TelegramBot().start_polling()

    def _handle_packages(self, client_root_path: Path) -> None:
        """
        Do all the job related to settings.PACKAGES
        """
        # get package list from settings
        pkgs = settings.PACKAGES[:]
        for pkg_name in pkgs:
            # get each package path in str format
            pkg_path = str(client_root_path / pkg_name)
            # append each package to sys.path
            sys.path.append(pkg_path)
            # load package
            self._load_pkg(pkg_path)

    def _load_pkg(self, name: str) -> None:
        """
        Recursively load package with all its modules given package's name.
        """
        # import the package
        pkg = __import__(name)
        for _, modname, is_pkg in pkgutil.iter_modules(
            pkg.__path__, pkg.__name__ + "."
        ):
            # if is_pkg, recursively load it
            if is_pkg:
                self._load_pkg(modname)
            # else just import it
            else:
                __import__(modname)


runner = _Runner()
