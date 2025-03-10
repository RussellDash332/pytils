# if v is a set
def mex(v):
    x = 0
    while x in v: x += 1
    return x

# if v is a list, create a sufficiently big boolean array
from array import *
a = array('b', [0]*30000)
def mex(s):
    for i in s: a[i] = 1
    for i in range(max(s)+2):
        if a[i] == 0:
            for j in s: a[j] = 0
            return i

# example state transition: take 1 or 2 stones
def states(x):
    return [x-i for i in (1, 2) if i <= x]

from functools import *
@cache
def grundy(x):
    if x == 0: return 0
    return mex({*map(grundy, states(x))})