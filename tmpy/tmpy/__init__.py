from math import fabs

import numpy as np


def zeros(length):
    return np.zeros(length, np.float64)


def solve(ma, mb, mc, v):
    """
    +   len(ma) == len(mb) == len(mc) == len(v)
    +   ma – po įstrižaine, rėžis: [1, len(v)-1], ma[0] == 0
    +   mb – įstrižainė, rėžis: [0, len(v)-1]
    +   mc – virš įstrižainės, rėžis: [0, len(v)-2], mc[len(v)-1] == 0
    +   v – vektorius, rėžis: [0, len(v)-1]
    """

    size = len(v)
    c = zeros(size)
    d = zeros(size)
    c[0] = -mc[0] / mb[0]
    d[0] = v[0] / mb[0]
    for i in range(1, size):
        divisor = ma[i] * c[i-1] + mb[i]
        c[i] = -mc[i] / divisor
        d[i] = (v[i] - ma[i] * d[i-1]) / divisor
    result = zeros(size)
    result[size-1] = d[size-1]
    for i in range(size - 2, -1, -1):
        result[i] = c[i] * result[i+1] + d[i]
    return result

def check_convergence(ma, mb, mc, v):
    assert(len(ma) == len(v) and len(mb) == len(v) and len(mc) == len(v))
    assert(ma[0] == 0 and mc[len(v)-1] == 0)
    exists_condition = False
    forall_condition = True
    for i in range(len(ma)):
        a = fabs(ma[i])
        b = mb[i]
        c = fabs(mc[i])
        forall_condition = forall_condition and (b >= a + c)
        exists_condition = exists_condition or (b > a + c)
    return forall_condition and exists_condition
