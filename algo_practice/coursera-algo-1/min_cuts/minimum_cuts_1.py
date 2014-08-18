#!/usr/bin/env python
from random import randint, choice
from copy import deepcopy
from math import log
import sys
import cProfile

original = {}
adj_list = {}
master = {}


def fuse(m, x):
    new_edge_list = []
    for i in adj_list[m] + adj_list[x]:
        if not (x == i or m == i):
            new_edge_list.append(i)
    adj_list[m] = new_edge_list
    master[x] = m
    del adj_list[x]


def cleanup(pivot):
    new_edge_list = []
    for i, x in enumerate(adj_list[pivot]):
        if x in adj_list:
            new_edge_list.append(x)
        else:
            while master[x] != x:
                x = master[x]
            if x != pivot:
                new_edge_list.append(x)
    adj_list[pivot] = new_edge_list


def random_contraction():
    if len(adj_list) <= 2:
        return
    while True:
        pivot = choice(adj_list.keys())
        cleanup(pivot)
        if len(adj_list[pivot]) > 0:
            break
    x = choice(adj_list[pivot])
    fuse(pivot, x)
    if len(adj_list) > 2:
        random_contraction()

def get_cuts():
    (k1, k2) = adj_list.keys()
    cleanup(k1)
    cleanup(k2)
    cnt = 0
    for i in adj_list[k2]:
        if i == k1:
            cnt += 1
    return cnt


def main_1():
    global original
    original = {}
    fd = open(sys.argv[1])
    for line in fd.readlines():
        line = line.strip('\n')
        line = line.strip()
        arr = [ int(x.strip()) for x in line.split('\t') ]
        a = arr.pop(0)
        if a not in original:
            original[a] = []
        for i in arr:
            if i not in original:
                original[i] = []
            original[a].append(i)

    n = len(original)
    number_of_trials = int((n ** 2) *  log(n)) + 1
    #number_of_trials = 100 # FIXME
    print 'Total number of tries: {}'.format(number_of_trials)
    minimum_cuts = False
    for i in range(number_of_trials):
        global adj_list
        adj_list = deepcopy(original)
        global master
        for key in adj_list:
            master[key] = key
        random_contraction()
        cuts = get_cuts()
        if not minimum_cuts or cuts < minimum_cuts:
            minimum_cuts = cuts
        print 'Cuts in {}th run is {}. Min cuts {}'.format(i + 1, cuts, minimum_cuts)
    print 'Minimum cut : {}'.format(minimum_cuts)
    return None
 

if __name__ == '__main__':
    cProfile.runctx('main_1()', None, locals())
    #main_1()


