# -*- coding: utf-8 -*-
import logging
try:
    from logging import NullHandler
except ImportError:
    from logging import Handler

    class NullHandler(Handler):
        def emit(self, record):
            pass


__version__ = '0.1.0'
__doc__ = """
My new project about that there must be silence in a library
"""

logging.getLogger('Silence_in_a_Library').addHandler(NullHandler())

