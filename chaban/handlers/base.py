import re

from .meta import MetaMH


class BaseMH(metaclass=MetaMH):
    class Meta:
        abstract = True

    def __init__(self, *args, **kwargs):
        self._meta = self.Meta()

    def _can_handle(self, message_text: str) -> bool:
        if re.search(self._regex, message_text) is None:
            return False
        return True

    @property
    def _regex(self) -> str:
        ...
