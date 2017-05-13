import random

import numpy as np

from timeit import timeit

from tmpy import solve as py_solve
from tmpy import check_convergence as py_check_convergence
from tmrs import solve as rs_solve
from tmrs import check_convergence as rs_check_convergence


def bench(stmt, setup):
    return timeit(stmt, setup=setup, number=100)


#array = lambda data: np.array(data, np.float64)
array = lambda data: data


def get_data():
    n = 4
    a = array([ 0, -1, -1, -1 ])
    b = array([ 4,  4,  4,  4 ])
    c = array([-1, -1, -1,  0 ])
    v = array([ 5,  5, 10, 23 ])
    return (a, b, c, v)


size = 10000
a = array([random.uniform(-1, 1) for i in range(size)])
a[0] = 0.0
b = array([random.uniform(2, 4) for i in range(size)])
c = array([random.uniform(-1, 1) for i in range(size)])
c[-1] = 0.0
v = array([random.uniform(-1, 1) for i in range(size)])


def get_large_data():
    return a, b, c, v


def print_time(name, time):
    print("{:10s}: {:.2f}".format(name, time))


def main_small():
    a, b, c, v = get_data()
    assert py_check_convergence(a, b, c, v)
    assert list(py_solve(a, b, c, v)) == [2, 3, 5, 7]
    time = bench('bench.py_solve(a, b, c, v)',
                 'import bench; a, b, c, v = bench.get_data()')
    print_time("Python", time)
    assert rs_check_convergence(a, b, c, v)
    assert list(rs_solve(a, b, c, v)) == [2, 3, 5, 7]
    time = bench('bench.rs_solve(a, b, c, v)',
                 'import bench; a, b, c, v = bench.get_data()')
    print_time("Rust", time)


def main_large():
    a, b, c, v = get_large_data()
    assert py_check_convergence(a, b, c, v)
    time = bench('bench.py_solve(a, b, c, v)',
                 'import bench; a, b, c, v = bench.get_large_data()')
    print_time("Python", time)
    assert rs_check_convergence(a, b, c, v)
    time = bench('bench.rs_solve(a, b, c, v)',
                 'import bench; a, b, c, v = bench.get_large_data()')
    print_time("Rust", time)


main = main_large
