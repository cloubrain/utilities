# -*- coding: utf-8 -*-
from collections import Iterable, Sequence
from datetime import datetime, timedelta
from itertools import islice
from copy import deepcopy

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

def slide(sequence, window=2):
    if isinstance(sequence, Sequence):
        iterator = iter(sequence)
    elif isinstance(sequence, Iterable):
        iterator = sequence
    else:
        iterator = iter(tuple())
    offset = max(1, min(window, 9))
    result = tuple(islice(iterator, offset))
    while len(result) == offset:
        yield result
        try:
            result = result[1:] + (iterator.next(), )
        except StopIteration as e:
            break

def time_range(start, stop, interval=1):
    ptr = deepcopy(start)
    while ptr < stop:
        yield ptr
        ptr += timedelta(hours=interval)

if __name__ == '__main__':
    test = (7, 1, 8, 0, 4, 5, 3, 12, 0, 0, 4, -14, 20, )
    for chunk in slide(test, window=5):
        print(chunk)

    start = datetime(2014, 1, 1, hour=0)
    stop = datetime(2014, 1, 1, hour=10)
    for curr_time in time_range(start, stop, interval=2):
        print(curr_time.strftime("%Y%m%d%H"))

