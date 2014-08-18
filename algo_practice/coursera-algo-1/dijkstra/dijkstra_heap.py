#!/usr/bin/env python
from heap import Heap

from random import randint, choice
from copy import deepcopy
from math import log
import sys

original = []
original_hash = {}

class Node(object):
    def __init__(self, x):
        self.x = x
        self.neigh = []
        self.processed = False
        self.shortest_distance = 0
        self.heap_index = -1
        self.shortest_path = []

    def add_neigh(self, y, length_xy):
        self.neigh.append((y, length_xy))

    def __str__(self):
        tmp_str = []
        for (i, dist) in self.neigh:
            tmp_str.append('({x} -> {y} : {dist})'.format(x = self.x, y = i.x, dist = dist))
        return '{x}  :  [ neigh: [{tmp_str}], processed: {processed}  dist : {dist} ]'.format \
                (x = self.x, tmp_str = ', '.join(tmp_str), processed = self.processed,
                 dist = self.shortest_distance)


def print_nodes(arr):
    for node in arr:
        print node

def get_add_node(x, input_arr):
    global original_hash
    if x not in original_hash:
        original_hash[x] = Node(x)
        input_arr.append(original_hash[x])
    return original_hash[x]

def has_unprocessed_neigh(cur_node):
    for node, dist in cur_node.neigh:
        if node.processed == False:
            return True
    return False

class DHeap(Heap):
    def compare(self, small, big):
        (n1, d1, s1) = self.arr[small]
        (n2, d2, s2) = self.arr[big]
        if (s1.shortest_distance + d1) < (s2.shortest_distance + d2):
            return True
        return False
    def swap(self, i, j):
        (n1, d1, s1) = self.arr[i]
        (n2, d2, s2) = self.arr[j]
        n1.heap_index = j
        n2.heap_index = i
        super(DHeap, self).swap(i, j)
    def move(self, x, y):
        # y = x
        (n1, d1, s1) = self.arr[x]
        (n2, d2, s2) = self.arr[y]
        n1.heap_index = y
        n2.heap_index = -1
        super(DHeap, self).move(x, y)
    def add(self, node):
        node[0].heap_index = super(DHeap, self).add(node)
        #print 'Added (n1 = {},\n\tdist = {},\n\tn2 = {})\n\t at {}'.format(node[0], node[1], node[2], node[0].heap_index)
    def del_node(self, node_index):
        self.arr[node_index][0].heap_index = -1
        super(DHeap, self).del_node(node_index)

def print_heap(dheap):
    for (end_node, dist, start_node) in dheap.arr:
        print (end_node.x, dist + start_node.shortest_distance),
    print

        

def compute_dijkstra_sp(start_node):
    print 'Computing all shortest path'
    dheap = DHeap()
    for (end_node, dist) in start_node.neigh:
        dheap.add((end_node, dist, start_node))
        print 'Adding {} to heap with dist{}'.format(end_node, dist + start_node.shortest_distance)
    print_heap(dheap)
    start_node.processed = True
    while True:
        tuple_values = dheap.get()
        if tuple_values == None:
            break
        (end_node, dist, start_node) = tuple_values
        #print 'Got (n1 = {},\n\tdist = {},\n\tn2 = {})\n'.format(end_node, dist, start_node)
        end_node.processed = True
        end_node.shortest_distance = start_node.shortest_distance + dist
        print 'Next {}'.format(end_node)
        print 'dist {}'.format(end_node.shortest_distance)
        print_heap(dheap)

        snode = end_node
        for (neigh, dist) in snode.neigh:
            if neigh.processed == True:
                continue
            if neigh.heap_index == -1:
                print 'Adding {} to heap with dist{}'.format(neigh, dist + snode.shortest_distance)
                dheap.add((neigh, dist, snode))
                print_heap(dheap)
            else:
                (x, old_dist, y) = dheap.arr[neigh.heap_index]
                #print (y.shortest_distance, old_dist, snode.shortest_distance, dist)
                if (y.shortest_distance + old_dist) > (snode.shortest_distance + dist):
                    dheap.del_node(neigh.heap_index)
                    print 'Re-adding {} to heap with dist{}'.format(neigh, dist + snode.shortest_distance)
                    dheap.add((neigh, dist, snode))
                    print_heap(dheap)
                else:
                    #print 'Ignoring - node {} already at pos {}'.format(x, neigh.heap_index)
                    pass
    print 'Done computing shortest path'


def read_array():
    global original
    fd = open(sys.argv[1])
    print 'Reading'
    for line in fd.readlines():
        line = line.strip('\n')
        line = line.strip()
        line_pairs = line.split('\t')
        a = int(line_pairs.pop(0))
        node = get_add_node(a, original)
        for i in line_pairs:
            lp = i.split(',')
            neigh = get_add_node(int(lp[0]), original)
            node.add_neigh(neigh, int(lp[1]))
    print 'Done reading'

def main_1():
    global original
    # Read array #
    read_array()
    #print_nodes(original)
    try:
        start_node = original_hash[int(sys.argv[2])]
    except:
        print 'Error finding start node'
        return
    compute_dijkstra_sp(start_node)
    original.sort(key = lambda x: x.x)
    #'''
    for i in original:
        '''
        if i.processed == False:
            print '1000000',
        else:
            print '{},'.format(i.shortest_distance),
        if i.processed == False:
            print '{}:1000000'.format(i.x),
        else:
            print '{}:{}'.format(i.x,i.shortest_distance)
        '''
        if i.x in [7,37,59,82,99,115,133,165,188,197]:
            if i.processed == False:
                print '1000000,',
            else:
                print '{},'.format(i.shortest_distance),
    #print_nodes(original)
    return None

if __name__ == '__main__':
    #import cProfile
    #cProfile.runctx('main_1()', None, locals())
    main_1()
