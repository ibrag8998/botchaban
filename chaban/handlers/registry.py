import typing as typ

from chaban.utils.singleton import SingletonMixin

from .base import BaseMH

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
