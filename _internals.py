# Private internals of singleton package
# This module is deleted by helpers.py

### --------- Import rewrite which prevents import of this module --------------- ###
'''
import builtins

_import = builtins.__import__


def new_import(name, globals=None, locals=None, fromlist=(), level=0):
    if name == 'singleton._internals':
        raise ImportError("module 'internals' of package 'singleton' is private")
    return _import(name, globals, locals, fromlist, level)
'''
### ------- Private attrs: mutable table dict and its portable setitem ------- ###    
from . import __init__

table = {}

def _table_setitem(key, value):
    table[key] = value
    