#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 01:33:42 2018

@author: jinyi
"""

from functools import reduce


# =============================================================================
# MAP
# apply some function to each element of a sequence
# return the modified list
# =============================================================================

n = [4, 3, 2, 1]
print(list(map(lambda x: x**2, n)))
# print(map(lambda x: x**2, n))
# print([x**2 for x in n])
# =============================================================================
# LAMBDA
# a simple 1-line functin
# do not use def or return keywords
# these are implicit
# =============================================================================

lambda x: 2*x  # parameter(s) : return
lambda x, y: x + y
mx = lambda x, y: x if x > y else y
print(mx(8, 5))

# =============================================================================
# filter
# filter imtes out of a sequence
# return filtered list
# =============================================================================

n = [4, 3, 2, 1]
print(list(filter(lambda x: x > 2, n)))
# print([x for x in n if x > 2])

# =============================================================================
# reduce
# applies some operations to imems of a sequence
# uses result of operation as first param of next operation
# returns an item, not a list.
# =============================================================================

n = [4, 3, 2, 1]
print(reduce(lambda x, y: x*y, n))






