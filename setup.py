# -*- coding: utf-8 -*-
from setuptools import setup

# This file is part of Utilities.
#
#     Utilities is free software: you can redistribute it and/or modify
#     it under the terms of the GNU Lesser General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#
#     Utilities is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU Lesser General Public License for more details.
#
#     You should have received a copy of the GNU Lesser General Public License
#     along with Utilities.  If not, see <http://www.gnu.org/licenses/>.

__author__ = 'horia margarit'

setup(
    version='0.1.0',
    name='Utilities',
    license='LICENSE.txt',
    author='Horia Margarit',
    include_package_data=True,
    test_suite='nose.collector',
    author_email='horia@cloubrain.com',
    tests_require="nose >= 1.3.4, < 2.0",
    scripts=('bin/structure_package.sh', ),
    packages=('utilities', 'utilities.tests', ),
    url='https://github.com/cloubrain/utilities',
    long_description=open('README.txt', mode='rb').read(),
    description='Provides a collection of classes and functions meant to assist the scientific '+\
                'and/or algorithmic minded Python programmer. As far as the authors know, '+\
                'these utilities are not currently present in the Python standard library.',
    install_requires=("blist >= 1.3.6, < 2.0", "numpy >= 1.9.0, < 2.0", "matplotlib >= 1.4.2, < 2.0", ),
)

