#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup
import versioneer

setup(
    name='ibpyte',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description='Python3 IbPy-like interface for the Interactive Brokers API',
    maintainer='Andrus Lepik',
    maintainer_email='alepik@gmail.com',
    url='https://github.com/misantroop/ibpyte',
    license='BSD License',
    packages=['ibpyte', 'ibpyte/lib', 'ibpyte/sym'],
)
