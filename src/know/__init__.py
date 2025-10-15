# This is free and unencumbered software released into the public domain.

"""The KNOW Framework for Python"""

import sys

assert sys.version_info >= (3, 9), "The KNOW Framework for Python requires Python 3.9+"

from ._version import __version__, __version_tuple__
from .classes import *
