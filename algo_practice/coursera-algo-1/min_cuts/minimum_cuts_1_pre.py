#!/usr/bin/env python
from random import randint, choice
from copy import deepcopy
from math import log
import sys
import cProfile


def fuse(m, x, adj_list):
    #print 'Fusing ({}) and ({})'.format(self.x, x.x)
    #for i in self.edges:
    #    print '({})'.format(i.x),
    #print ''
    new_edge_list = []
    for i in adj_list[m]:
        if not x == i:
            new_edge_list.append(i)
    for x_neigh in adj_list[x]:
        if not m == x_neigh:
            new_edge_list.append(x_neigh)
        for i in range(len(adj_list[x_neigh])):
            if adj_list[x_neigh][i] == x:
                adj_list[x_neigh][i] = m
    adj_list[m] = new_edge_list
    #for i in m.edges:
    #    print '({})'.format(i.x),
    #print ''
    #print 'Done'



'''
    def __str__(self):
        str_tmp = []
        for i in self.edges:
            str_tmp.append('({})'.format(i.x))
        fused_tmp = []
        for i in self.fused_nodes:
            fused_tmp.append('({})'.format(i.x))
        return '[ ({}) : {str_tmp} : Fused Nodes: {fused_tmp} ]'.format(self.x, str_tmp = str_tmp, fused_tmp = fused_tmp)
'''

def print_adj_list(adj_list):
    for node in adj_list:
        print adj_list[node]


def random_contraction(adj_list):
    if len(adj_list) <= 2:
        return
    pivot = choice(adj_list.keys())
    x = choice(adj_list[pivot])
    #print '--------'
    #print 'Contracting {} and {}'.format(adj_list[pivot], adj_list[x.x])
    fuse(pivot, x, adj_list)
    del adj_list[x]
    #print 'After Contraction'
    #print_adj_list(adj_list)
    #print '--------'
    if len(adj_list) > 2:
        random_contraction(adj_list)


def main_1():
    adj_list = {}
    fd = open(sys.argv[1])
    for line in fd.readlines():
        line = line.strip('\n')
        line = line.strip()
        arr = [ int(x.strip()) for x in line.split('\t') ]
        a = arr.pop(0)
        if a not in adj_list:
            adj_list[a] = []
        for i in arr:
            if i not in adj_list:
                adj_list[i] = []
            adj_list[a].append(i)
    original = adj_list
    #print_adj_list(adj_list)

    n = len(adj_list)
    #number_of_trials = int((n ** 2) *  log(n)) + 1
    number_of_trials = int((n ** 2))
    number_of_trials = 5 # FIXME
    print 'Total number of tries: {}'.format(number_of_trials)
    minimum_cuts = False
    for i in range(number_of_trials):
        adj_list = deepcopy(original)
        #print_adj_list(adj_list)
        random_contraction(adj_list)
        #print_adj_list(adj_list)
        for k in adj_list:
            cuts = len(adj_list[k])
        if not minimum_cuts or cuts < minimum_cuts:
            minimum_cuts = cuts
        print 'Cuts in {}th run is {}. Min cuts {}'.format(i + 1, cuts, minimum_cuts)
    print 'Minimum cut : {}'.format(minimum_cuts)
    return None
 

if __name__ == '__main__':
    #profile.run('main_1()')
    cProfile.runctx('main_1()', None, locals())
    #main_1()


