# -*- coding: utf-8 -*-
from utilities.iterators import slide
from nose.tools import assert_equal

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


class TestSlide(object):

    @classmethod
    def setUpAll(cls):
        cls.__data = (7, 0, 4, 5, 1, )

    @classmethod
    def tearDownAll(cls):
        del cls.__data

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_default_window(self):
        result = tuple(slide(self.__data))
        expectation = ((7, 0, ),
                       (0, 4, ),
                       (4, 5, ),
                       (5, 1, ),
                      )
        assert_equal(result, expectation)

    def test_triplet_window(self):
        result = tuple(slide(self.__data, window=3))
        expectation = ((7, 0, 4, ),
                       (0, 4, 5, ),
                       (4, 5, 1, ),
                      )
        assert_equal(result, expectation)


class TestTimeRange(object):

    @classmethod
    def setUpAll(cls):
        pass

    @classmethod
    def tearDownAll(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

