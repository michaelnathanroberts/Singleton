from . import helpers

import abc

Singleton = None

class SingletonMeta(abc.ABCMeta):
    "Metaclass for Singleton"
    def __call__(cls, *args, **kwds):
        first = not helpers.instance_present(cls)
        obj = helpers.get_instance(cls)
        if first:
            obj.__init__(*args, **kwds)
        return obj
    
    def __new__(metacls, name, bases, classdict):
        if Singleton is not None:
            for b in bases:
                if b in Singleton.__mro__ and not helpers.is_abstract(b) and b is not Singleton:
                    raise TypeError("Concrete singleton classes may not be subclassed")
        if '__slots__' not in classdict:
            classdict['__slots__'] = ()
        cls = type.__new__(metacls, name, bases, classdict)
        if Singleton is not None:
            if Singleton not in cls.mro():
                raise TypeError("Singleton classes must inherit from Singleton")
        return cls
    

class Singleton(metaclass=SingletonMeta):
    """Base class of all singleton types.
    A singleton type only has one instance, which is lazily generated.
    """
    __slots__ = ()

del _internals