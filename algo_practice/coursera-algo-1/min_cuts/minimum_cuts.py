#!/usr/bin/env python
from random import randint, choice
from copy import deepcopy
from math import log
import sys


class Node(object):
    def __init__(self, x):
        self.x = x
        self.edges = []
        self.fused_nodes = []

    def __eq__(self, b):
        if type(b) == type(0):
            return self.x == b
        else:
            return self.x == b.x

    def fuse(self, x):
        #print 'Fusing ({}) and ({})'.format(self.x, x.x)
        #for i in self.edges:
        #    print '({})'.format(i.x),
        #print ''
        self.fused_nodes.extend(x.fused_nodes)
        self.fused_nodes.append(Node(x.x))
        new_edge_list = []
        for i in self.edges:
            if not x == i:
                new_edge_list.append(i)
        for x_neigh in x.edges:
            if not self == x_neigh:
                new_edge_list.append(x_neigh)
            for i in range(len(x_neigh.edges)):
                if x_neigh.edges[i] == x:
                    x_neigh.edges[i] = self
        self.edges = new_edge_list
        #for i in self.edges:
        #    print '({})'.format(i.x),
        #print ''
        #print 'Done'


    def add_edge(self, n):
        if not n == self:
            self.edges.append(n)

    def __str__(self):
        str_tmp = []
        for i in self.edges:
            str_tmp.append('({})'.format(i.x))
        fused_tmp = []
        for i in self.fused_nodes:
            fused_tmp.append('({})'.format(i.x))
        return '[ ({}) : {str_tmp} : Fused Nodes: {fused_tmp} ]'.format(self.x, str_tmp = str_tmp, fused_tmp = fused_tmp)


def print_adj_list(adj_list):
    for node in adj_list:
        print adj_list[node]


def random_contraction(adj_list):
    if len(adj_list) <= 2:
        return
    pivot = choice(adj_list.keys())
    x = choice(adj_list[pivot].edges)
    #print '--------'
    #print 'Contracting {} and {}'.format(adj_list[pivot], adj_list[x.x])
    adj_list[pivot].fuse(x)
    del adj_list[x.x]
    #print 'After Contraction'
    #print_adj_list(adj_list)
    #print '--------'
    if len(adj_list) > 2:
        random_contraction(adj_list)


if __name__ == '__main__':
    adj_list = {}
    fd = open(sys.argv[1])
    for line in fd.readlines():
        line = line.strip('\n')
        line = line.strip()
        arr = [ int(x.strip()) for x in line.split('\t') ]
        a = arr.pop(0)
        if a not in adj_list:
            adj_list[a] = Node(a)
        for i in arr:
            if i not in adj_list:
                adj_list[i] = Node(i)
            adj_list[a].add_edge(adj_list[i])
    original = adj_list
    print_adj_list(adj_list)

    n = len(adj_list)
    #number_of_trials = int((n ** 2) *  log(n)) + 1
    number_of_trials = int((n ** 2))
    print 'Total number of tries: {}'.format(number_of_trials)
    minimum_cuts = False
    for i in range(number_of_trials):
        adj_list = deepcopy(original)
        #print_adj_list(adj_list)
        random_contraction(adj_list)
        #print_adj_list(adj_list)
        for k in adj_list:
            cuts = len(adj_list[k].edges)
        if not minimum_cuts or cuts < minimum_cuts:
            minimum_cuts = cuts
        print 'Cuts in {}th run is {}. Min cuts {}'.format(i + 1, cuts, minimum_cuts)
    print 'Minimum cut : {}'.format(minimum_cuts)
        


