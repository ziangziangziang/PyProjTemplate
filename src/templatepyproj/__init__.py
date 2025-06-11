from .module1 import do_nothing
from .module2 import say_hello
from importlib import metadata
from ._version import (
    __version__,
    __version_tuple__,
    version,
    version_tuple,
)
__all__ = ["do_nothing", "say_hello"]
