"Helper functions for SingletonMeta"

from . import _internals
# import builtins
# import functools
import types
import sys

def get_instance(cls, *args, **kwds):
    """Return the sole instance of a singleton class
    Use on a non-singleton class is discouraged.
    """
    if not instance_present(cls):
        for b in cls.mro()[::-1]:
            try:
                obj = b.__new__(cls, *args, **kwds)
            except TypeError as e:
                if 'is not safe, use' not in e.args[0]:
                    raise
            else:
                break
        obj.__init__(*args, **kwds)
        _internals._table_setitem(cls, obj)
    return table[cls]


def instance_present(cls):
    """Return if cls' instance has been generated.
    If cls is not a Singleton class, this function will always return False.
    """
    return cls in table

def is_abstract(cls):
    "Return is cls is abstract."
    return bool(getattr(cls, '__abstractmethods__', False))

table = types.MappingProxyType(_internals.table)

sys.modules['singleton._internals'] = NotImplemented

'''# Prohibit importing _internals module
for attr in (*functools.WRAPPER_ASSIGNMENTS, *functools.WRAPPER_UPDATES):
    setattr(_internals.new_import, attr, getattr(builtins.__import__, attr, {}))
builtins.__import__ = _internals.new_import'''

# Delete internals module
del  _internals