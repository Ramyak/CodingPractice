#!/usr/bin/env python
from random import randint, choice
from copy import deepcopy
from math import log
import sys

original = []
original_hash = {}
frontier = []

class Node(object):
    def __init__(self, x):
        self.x = x
        self.neigh = []
        self.processed = False
        self.shortest_distance = 0
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

def compute_dijkstra_sp():
    print 'Computing all shortest path'
    while len(frontier) > 0:
        shortest_path_edge = None
        shortest_path = -1
        cleanup_index = []
        for i in range(len(frontier)):
            cur_start_node = frontier[i]
            cleanup_flag = True
            for (cur_end_node, cur_dist) in cur_start_node.neigh:
                if cur_end_node.processed:
                    continue
                cleanup_flag = False
                if shortest_path == -1 or shortest_path > \
                        (cur_start_node.shortest_distance + cur_dist):
                            shortest_path_edge = cur_end_node
                            shortest_path = cur_start_node.shortest_distance + cur_dist
            if cleanup_flag:
                cleanup_index.append(i)
        if shortest_path > -1:
            # Cleanup shortest_path_edge and add it to frontier #
            if has_unprocessed_neigh(shortest_path_edge):
                frontier.append(shortest_path_edge)
            shortest_path_edge.processed = True
            shortest_path_edge.shortest_distance = shortest_path
            print 'Next {}'.format(shortest_path_edge)
            print 'dist {}'.format(shortest_path_edge.shortest_distance)
        # Cleanup #
        cleanup_index.reverse()
        for i in cleanup_index:
            del frontier[i]
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
    frontier.append(start_node)
    start_node.processed = True
    compute_dijkstra_sp()
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
 
