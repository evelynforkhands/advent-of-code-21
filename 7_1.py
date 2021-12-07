import numpy as np


def read_input():
    f = open('inputs/test.txt', 'r')
    return [int(x) for x in f.read().split(',')]


crabs = read_input()
opt = int(np.median(crabs))
print(sum([abs(x - opt) for x in crabs]))
