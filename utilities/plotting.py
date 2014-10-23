# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from itertools import izip
from numpy import linspace

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

def horizontal_bar(groups, values, **kwargs):
    if 'axes' in kwargs:
        ax = kwargs.pop('axes')
    else:
        ax = plt.figure().add_subplot(111)
    labels = kwargs.pop('bar_labels', None)
    spacing = kwargs.pop('bar_spacing', 0.2)
    thickness = kwargs.pop('bar_thickness', 0.8)
    offset = kwargs.pop('offset_from_axis', 0.0)
    group_spread = kwargs.pop('group_spread', 0.2)
    init_group_pos = spacing
    for name, group_vals in izip(groups, values):
        n_bars = len(group_vals)
        group_height = ((thickness + spacing) * n_bars)
        pos = linspace(init_group_pos, init_group_pos + group_height,
                       endpoint=False, num=n_bars, retstep=False)
        if labels is not None:
            ax.set_yticks(pos, labels)
        ax.barh(pos, group_vals, height=thickness, left=offset, **kwargs)
        init_group_pos += thickness + spacing + group_spread
    return ax

def vertical_bar(groups, values, **kwargs):
    if 'axes' in kwargs:
        ax = kwargs.pop('axes')
    else:
        ax = plt.figure().add_subplot(111)
    labels = kwargs.pop('bar_labels', None)
    spacing = kwargs.pop('bar_spacing', 0.2)
    thickness = kwargs.pop('bar_thickness', 0.8)
    offset = kwargs.pop('offset_from_axis', 0.0)
    group_spread = kwargs.pop('group_spread', 0.2)
    init_group_pos = spacing
    for name, group_vals in izip(groups, values):
        n_bars = len(group_vals)
        group_width = ((thickness + spacing) * n_bars)
        pos = linspace(init_group_pos, init_group_pos + group_width,
                       endpoint=False, num=n_bars, retstep=False)
        if labels is not None:
            ax.set_xticks(pos, labels)
        ax.bar(pos, group_vals, width=thickness, bottom=offset, **kwargs)
        init_group_pos += thickness + spacing + group_spread
    return ax

