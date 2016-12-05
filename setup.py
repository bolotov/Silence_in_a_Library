# -*- coding: utf-8 -*-
import sys
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

sys.path.insert(0, '.')
from Silence_in_a_Library import __version__, __doc__


setup(
    name="Silence_in_a_Library",
    version=__version__,
    description=__doc__,
    packages=["Silence_in_a_Libraryrary"],
    platforms=["any"],
    classifiers=[
          'Development Status :: 1 - Planning',
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: Implementation :: CPython',
          'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
