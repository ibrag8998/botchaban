from .base import BaseMH
from .registry import mh_registry


class MH(BaseMH):
    registry = mh_registry

    class Meta:
        abstract = True
