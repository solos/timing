#!/usr/bin/env python
#coding=utf-8

from distutils.core import setup
import timing

setup(name='timing',
      version=timing.__version__,
      description='Timing decorator for functions',
      long_description=timing.__doc__,
      author=timing.__author__,
      author_email='solos@solos.so',
      py_modules=['timing'],
      scripts=['timing.py'],
      license='MIT',
      platforms=['any'],
      url='https://github.com/solos/timing')
