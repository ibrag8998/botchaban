import re
import typing as typ

from chaban.actions import Action
from chaban.utils import MetaSingleton

from .exceptions import NoHandlersRegistered


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
    action: Action

    class Meta:
        abstract = True

    @classmethod
    def can_handle(cls, message: typ.Dict[str, typ.Any]) -> bool:
        ...

    @classmethod
    def get_message_content(
        cls, message: typ.Dict[str, typ.Any], key: str, err_message: str = None
    ) -> typ.Union[str, typ.Dict[str, typ.Any], typ.Any]:
        try:
            return message[key]
        except KeyError:
            if err_message is None:
                err_message = "You specified wrong handler"
            raise TypeError(err_message)


_MHType = typ.Type[BaseMH]
_MHList = typ.List[_MHType]


class _MHRegistry(metaclass=MetaSingleton):
    _mhs: _MHList = []

    def get_handler_and_handle(self, message) -> None:
        mh = self._get_mh(message)

        if mh is None:
            return

        mh.action.act(message)

    @property
    def mhs(self) -> _MHList:
        return self._mhs[:]

    def add(self, mh: _MHType) -> None:
        """
        Add message handler like this:

        ```
            mh_registry.add(MyMH)
        ```
        """
        self._mhs.append(mh)

    def __le__(self, mh: _MHType) -> None:
        """
        Add message handler like this:

        ```
            mh_registry <= MyMH
        ```
        """
        self.add(mh)

    def _get_mh(self, message) -> typ.Optional[_MHType]:
        if len(self.mhs) == 0:
            raise NoHandlersRegistered("You didn't registered any message handlers")

        for mh in self.mhs:
            if mh.can_handle(message):
                return mh

        return None


mh_registry = _MHRegistry()
