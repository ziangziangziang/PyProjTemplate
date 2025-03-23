from .module1 import do_nothing
from .module2 import say_hello
from importlib import metadata
__version__ = metadata.version(__name__)
__all__ = ["do_nothing", "say_hello"]