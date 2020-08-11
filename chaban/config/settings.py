import os
import typing as typ
from pathlib import Path

from chaban.core.exceptions import ImproperlyConfiguredError
from chaban.utils import SingletonMixin

from . import global_settings


class Settings(SingletonMixin):
    TELEGRAM_TOKEN: str
    BASE_DIR: typ.Union[str, Path]
    PACKAGES: typ.List[str]

    _settings_module = None
    _cache: typ.Dict[str, typ.Any] = {}

    def __getattr__(self, name: str) -> typ.Any:
        if self._settings_module is None:
            self._setup()

        if name not in self._cache:
            self._cache[name] = getattr(self._settings_module, name)

        return self._cache[name]

    def _setup(self) -> None:
        env_var_name = global_settings.CHABAN_SETTINGS_MODULE_ENV_VAR
        settings_env = os.getenv(env_var_name)
        if settings_env is None:
            raise ImproperlyConfiguredError(
                "{} env var is required, but not set".format(env_var_name)
            )

        self._settings_module = __import__(settings_env)


settings = Settings()
