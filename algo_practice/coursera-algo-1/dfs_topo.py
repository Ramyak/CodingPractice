#!/usr/bin/env python
from random import randint, choice
from copy import deepcopy
from math import log
import sys
import cProfile

original = []
torder = 0

class Node(object):
    def __init__(self, x, parent = None, torder = None, marked = False):
        self.x = x
        self.neigh = []
        self.parent = parent
        self.torder = torder
        self.marked = False
    def __eq__(self, x):
        return self.x == x
    def add_neigh(self, node):
        self.neigh.append(node)
    def __str__(self):
        neigh_str = ', '.join([str(i.x) for i in self.neigh])
        return '[{x} :  neigh = {neigh} torder = {torder} ]'.format(x = self.x, neigh =neigh_str, torder = self.torder)

def get_add_node(x, input_arr):
    for i in input_arr:
        if i == x:
            return i
    i = Node(x)
    input_arr.append(i)
    return i


def print_nodes(arr):
    for i in arr:
        print i

def dfs(node):
    global torder
    for i in node.neigh:
        if i.marked == False:
            i.marked = True
            dfs(i)
    node.torder = torder
    torder -= 1


def main_1():
    global original
    global torder
    fd = open(sys.argv[1])
    for line in fd.readlines():
        line = line.strip('\n')
        line = line.strip()
        arr = [ int(x.strip()) for x in line.split('\t') ]
        a = arr.pop(0)
        node = get_add_node(a, original)
        for i in arr:
            # original #
            neigh = get_add_node(i, original)
            node.add_neigh(neigh)
    torder = len(original)
    dfs(original[0])
    original.sort(key = lambda x: x.torder)
    print_nodes(original)
    return None

if __name__ == '__main__':
    #cProfile.runctx('main_1()', None, locals())
    main_1()
 
