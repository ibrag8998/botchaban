import typing as typ

from .base import BaseMH


class RegexMH(BaseMH):
    regex: str

    class Meta:
        abstract = True

    @property
    def _regex(self) -> str:
        return self.regex


class CommandMH(BaseMH):
    command: str
    args: typ.List[str] = []
    must_start_with_command: bool = True
    allow_trailing_symbols: bool = False

    class Meta:
        abstract = True

    @property
    def _regex(self) -> str:
        n_args = len(self.args)
        return "{}/{}{}{}".format(
            "^" if self.must_start_with_command else "",
            self.command.lstrip("/"),
            r" [0-9a-zA-Z_]+" * n_args,
            "$" if not self.allow_trailing_symbols else "",
        )
