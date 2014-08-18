#!/usr/bin/env python
from random import randint, choice
from copy import deepcopy
from math import log
import sys
import cProfile

original = []


class Node(object):
    def __init__(self, x, parent = None, layer = None, marked = False):
        self.x = x
        self.neigh = []
        self.parent = parent
        self.layer = layer
        self.marked = False
    def __eq__(self, x):
        return self.x == x
    def add_neigh(self, node):
        self.neigh.append(node)
    def __str__(self):
        neigh_str = ', '.join([str(i.x) for i in self.neigh])
        return '[{x} :  neigh = {neigh} layer = {layer} ]'.format(x = self.x, neigh =neigh_str, layer = self.layer)

def get_add_node(x):
    for i in original:
        if i == x:
            return i
    i = Node(x)
    original.append(i)
    return i


def print_nodes(arr):
    for i in arr:
        print i


def main_1():
    global original
    original = []
    queue = []
    fd = open(sys.argv[1])
    for line in fd.readlines():
        line = line.strip('\n')
        line = line.strip()
        arr = [ int(x.strip()) for x in line.split('\t') ]
        a = arr.pop(0)
        node = get_add_node(a)
        for i in arr:
            neigh = get_add_node(i)
            node.add_neigh(neigh)
    queue.append(original[0])

    while len(queue) > 0:
        new_frontier = queue.pop(0)
        if new_frontier.marked == False:
            new_frontier.marked = True
            if new_frontier.parent:
                new_frontier.layer = new_frontier.parent.layer + 1
            else:
                new_frontier.layer = 1
            for i in new_frontier.neigh:
                i.parent = new_frontier
                queue.append(i)
    original.sort(key = lambda x: x.layer)
    print_nodes(original)
    return None

if __name__ == '__main__':
    cProfile.runctx('main_1()', None, locals())
 
