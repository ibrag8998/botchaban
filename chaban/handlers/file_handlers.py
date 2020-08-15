import re
import typing as typ

from .base import BaseMH


class _BaseFileMH(BaseMH):
    class Meta:
        abstract = True

    @classmethod
    def can_handle(cls, message: typ.Dict[str, typ.Any]) -> bool:
        # get document
        message_file = cls.get_message_content(message, "document")
        # get file_name from document
        file_name = message_file["file_name"]

        return cls.validate_file_name(file_name)

    @classmethod
    def validate_file_name(cls, file_name: str) -> bool:
        ...


class FileNameMH(_BaseFileMH):
    # should be regular expression
    file_name_pat: str

    class Meta:
        abstract = True

    @classmethod
    def validate_file_name(cls, file_name: str) -> bool:
        # check if ``cls.file_name_pat`` matches actual `file_name`
        if re.search(cls.file_name_pat, file_name) is not None:
            return True

        # return False otherwise
        return False


class FileTypeMH(_BaseFileMH):
    # file_type should be something like "pdf" or "txt",
    # but it can also contain dot, like ".mp4"
    file_type: str

    class Meta:
        abstract = True

    @classmethod
    def validate_file_name(cls, file_name: str) -> bool:
        # split the file name with dot
        *rest, file_ext = file_name.split(".")

        # if there are no dots in file_name, `rest` will be [].
        if len(rest) == 0:
            return False

        # check if ``cls.file_type`` matches the actual `file_ext`
        if file_ext == cls.file_type.lstrip("."):
            return True

        # return False otherwise
        return False
