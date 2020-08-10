import typing as typ

from .base import BaseMH


class RegexMH(BaseMH):
    regex: str

    class Meta:
        abstract = True

    @classmethod
    def _get_regex(cls) -> str:
        return cls.regex


class CommandMH(BaseMH):
    command: str
    args: typ.List[str] = []
    must_start_with_command: bool = True
    allow_trailing_symbols: bool = False

    class Meta:
        abstract = True

    @classmethod
    def _get_regex(cls) -> str:
        n_args = len(cls.args)
        return "{}/{}{}{}".format(
            "^" if cls.must_start_with_command else "",
            cls.command.lstrip("/"),
            r" [0-9a-zA-Z_]+" * n_args,
            "$" if not cls.allow_trailing_symbols else "",
        )
