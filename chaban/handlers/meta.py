import typing as typ


class MetaMH(type):
    class __DefaultMeta:
        abstract = False

    def __new__(
        cls, name: str, bases: typ.Tuple[type, ...], attrs: typ.Dict[str, typ.Any]
    ):
        # make alias for super new
        super_new = super().__new__

        # get `class Meta: ...` from subclass
        Meta = attrs.get("Meta")

        # Meta may be undefined check it
        if Meta is None:
            Meta = cls.__DefaultMeta
        else:
            # Meta may be not a class, who knows what client want to do ...
            if not isinstance(Meta, type):
                return super_new(cls, name, bases, attrs)
            # ok, Meta is defined, it is a class, now set some default attrs which was
            # not set manually by clients
            else:
                for attr_name, attr in cls.__DefaultMeta.__dict__.items():
                    if not hasattr(Meta, attr_name):
                        setattr(Meta, attr_name, attr)

        attrs["Meta"] = Meta

        # return new class
        return super_new(cls, name, bases, attrs)
