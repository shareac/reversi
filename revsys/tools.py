class _ConstMeta(type):
    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise TypeError(f"Can't rebind const ({name})")
        else:
            self.__setattr__

class Const(metaclass=_ConstMeta):
     pass
