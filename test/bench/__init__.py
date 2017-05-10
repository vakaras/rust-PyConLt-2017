import numpy as np

from timeit import timeit

from tmpy import solve as py_solve
from tmpy import check_convergence


def get_data():
    #array = lambda data: np.array(data, np.float64)
    array = lambda data: data
    n = 4
    a = array([ 0, -1, -1, -1 ])
    b = array([ 4,  4,  4,  4 ])
    c = array([-1, -1, -1,  0 ])
    v = array([ 5,  5, 10, 23 ])
    return (a, b, c, v)

def print_time(name, time):
    print("{:10s}: {:.2f}".format(name, time))


def main():
    a, b, c, v = get_data()
    assert check_convergence(a, b, c, v)
    assert list(py_solve(a, b, c, v)) == [2, 3, 5, 7]
    time = timeit('bench.py_solve(a, b, c, v)',
                  setup='import bench; a, b, c, v = bench.get_data()')
    print_time("Python", time)
