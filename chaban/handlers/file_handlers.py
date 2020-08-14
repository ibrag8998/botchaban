import re
import typing as typ

from .base import BaseMH


class FileMH(BaseMH):
    file_name_pat: str

    class Meta:
        abstract = True

    @classmethod
    def can_handle(cls, message: typ.Dict[str, typ.Any]) -> bool:
        # get document
        message_file = message["document"]
        # get file_name from document
        file_name = message_file["file_name"]

        if re.search(cls.file_name_pat, file_name) is None:
            return False
        return True
