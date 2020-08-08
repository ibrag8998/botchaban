import re
import typing as typ

from chaban.utils.singleton import SingletonMixin


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
            Meta.__name__ = "Meta"
        else:
            # Meta may be not a class, who knows what client want to do ...
            if not isinstance(Meta, type):
                return super_new(cls, name, bases, attrs)
            # ok, Meta is defined and it is a class, now set some default attrs which
            # was not set manually by clients
            else:
                for attr_name, attr in cls.__DefaultMeta.__dict__.items():
                    if not hasattr(Meta, attr_name):
                        setattr(Meta, attr_name, attr)

        # manipulate attrs
        attrs["Meta"] = Meta

        # now, initialize new class
        new_cls = super_new(cls, name, bases, attrs)

        # add to registry if it is not abstract
        if not Meta.abstract:  # type: ignore
            mh_registry.add(new_cls)

        # return new class
        return new_cls


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


_MHType = typ.Type[BaseMH]
_MHList = typ.List[_MHType]


class _MHRegistry(SingletonMixin):
    _mhs: _MHList = []

    @property
    def mhs(self) -> _MHList:
        return self._mhs[:]

    def add(self, mh: _MHType):
        self._mhs.append(mh)


mh_registry = _MHRegistry()
