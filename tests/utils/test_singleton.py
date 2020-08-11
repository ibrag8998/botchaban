from chaban.utils import MetaSingleton


class _Helper(metaclass=MetaSingleton):
    def __init__(self, a):
        self.a = a


def test_attrs():
    x = _Helper(1)
    y = _Helper(2)
    assert x.a == y.a == 1


def test_is():
    x = _Helper(1)
    y = _Helper(2)
    assert x is y
