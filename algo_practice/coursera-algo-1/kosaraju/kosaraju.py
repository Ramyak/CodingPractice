#!/usr/bin/env python
from random import randint, choice
from copy import deepcopy
from math import log
import sys


original = []
leader = None
ftime = 0
original_ftime = []
original_hash = {}

class Node(object):
    def __init__(self, x, nleader = None, ftime = None, marked = False):
        self.x = x
        self.neigh = []
        self.rneigh = []
        self.nleader = nleader
        self.ftime = ftime
        self.marked = False
    def __eq__(self, x):
        return self.x == x
    def add_neigh(self, node):
        self.neigh.append(node)
    def add_rneigh(self, node):
        self.rneigh.append(node)
    def __str__(self):
        neigh_str = ', '.join([str(i.x) for i in self.neigh])
        return '[{x} :  neigh = {neigh} nleader = {nleader} ftime = {ftime} ]' \
                .format(x=self.x, neigh=neigh_str, nleader=self.nleader.x if self.nleader else None,
                        ftime=self.ftime)

def get_add_node(x, input_arr):
    global original_hash
    if x not in original_hash:
        original_hash[x] = Node(x)
        input_arr.append(original_hash[x])
    return original_hash[x]


def print_nodes(arr):
    for i in arr:
        print i

def dfs_1(node, reverse):
    global ftime
    global leader
    global original_ftime
    node.marked = True
    node.nleader = leader
    arr = node.rneigh if reverse else node.neigh
    for i in arr:
        if i.marked == False:
            dfs_1(i, reverse)
    ftime += 1
    node.ftime = ftime
    if reverse:
        original_ftime[ftime - 1] = node

def dfs_loop():
    global leader
    global original_ftime 
    original_ftime = [None] * len(original)
    for node in reversed(original):
        if node.marked == False:
            leader = node
            dfs_1(node, reverse = True)
    for node in original_ftime:
        node.marked = False
        node.nleader = None
    for node in reversed(original_ftime):
        if node.marked == False:
            leader = node
            dfs_1(node, reverse = False)


def count_leaders():
    from collections import Counter
    leader_arr = []
    for i in original_ftime:
        leader_arr.append(i.nleader.x)
    return Counter(leader_arr).most_common(5)


def read_array():
    global original
    fd = open(sys.argv[1])
    print 'Reading'
    for line in fd.readlines():
        line = line.strip('\n')
        line = line.strip()
        arr = [ int(x.strip()) for x in line.split(' ') ]
        a = arr.pop(0)
        node = get_add_node(a, original)
        for i in arr:
            neigh = get_add_node(i, original)
            node.add_neigh(neigh)
            neigh.add_rneigh(node) # reverse edge
        print a

def main_1():
    global original
    # Read array #
    read_array()
    print 'Done reading'
    dfs_loop()
    print 'Done dfs_loop'
    print count_leaders()
    return None

if __name__ == '__main__':
    #import cProfile
    #cProfile.runctx('main_1()', None, locals())
    import sys
    import threading
    threading.stack_size(67108864)
    sys.setrecursionlimit(2**20)
    thread = threading.Thread(target=main_1)
    thread.start()
 
