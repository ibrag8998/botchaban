import typing as typ

from .base import BaseMH


class WildcardMH(BaseMH):
    class Meta:
        abstract = True

    @classmethod
    def can_handle(cls, message: typ.Dict[str, typ.Any]) -> bool:
        return True
