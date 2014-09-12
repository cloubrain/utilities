# -*- coding: utf-8 -*-
from itertools import chain, islice
from collections import deque
from math import ceil, floor
from iterators import slide
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


class MovingAverage(object):

    def __init__(self, _type, alpha=None, n_samples=None, warm_up=False):
        self.__alpha = 0.40 if alpha is None else alpha
        self.__start = -5 if n_samples is None else (-1 * n_samples)
        self.__exp_bootstrap = 1 if not warm_up else (5 if n_samples is None else n_samples)
        if _type == 'exponential':
            setattr(self, 'process', self.__exponential)
        elif _type == 'simple':
            setattr(self, 'process', self.__simple)
        else:
            raise NotImplementedError("only 'exponential' and 'simple' moving averages currently supported!")

    def __call__(self, args):
        self.process(args)

    def __simple(self, args):
        avg = 0.00
        for _list in slide(args, window=abs(self.__start)):
            avg = sum(_list) / float(abs(self.__start))
        self.value = deepcopy(avg)

    def __exponential(self, args):
        first = list(islice(args, self.__exp_bootstrap))
        avg = sum(first) / float(self.__exp_bootstrap)
        for elem in chain(first[1:], args):
            avg = (self.__alpha * elem) + ((1.0 - self.__alpha) * avg)
        self.value = deepcopy(avg)


def compute_quartiles(_list):
    """
        Invariant: _list is sorted in application specific order
    """
    quartiles = dict()
    stack = deque([("50%", 0, len(_list), )])
    while len(stack):
        key, start, stop = stack.popleft()
        if (stop - start) % 2:
            mid_point = (stop - start - 1) / 2
            left = mid_point
            right = mid_point
            median = float(_list[mid_point + start])
        else:
            mid_point = (stop - start - 1) / 2.00
            left = int(floor(mid_point))
            right = int(ceil(mid_point))
            median = (_list[left + start] + _list[right + start]) / 2.00
        quartiles[key] = median
        if key == "50%":
            stack.appendleft(("25%", start, left, ))
            stack.appendleft(("75%", right + 1, stop))
    return quartiles

if __name__ == '__main__':
    try:
        import simplejson as json
    except ImportError:
        import json

    test = (7, 1, 8, 0, 4, 5, 3, 12, 0, 0, 4, -14, 20, )
    ema = MovingAverage('exponential', alpha=0.20, warm_up=True)
    sma = MovingAverage('simple', n_samples=10)
    ema(test)
    sma(test)
    print(ema.value)
    print(sma.value)

    print(json.dumps(compute_quartiles(sorted(test)), sort_keys=True))

