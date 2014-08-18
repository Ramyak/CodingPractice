#!/usr/bin/env python
from random import randint, choice
import sys


class Vertex(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.edges = []
        self.fused_nodes = []

    def __eq__(self, b):
        return self.x == b.x and self.y == b.y

    def fuse(self, x):
        print 'Fusing ({}, {}) and ({}, {})'.format(self.x, self.y, x.x, x.y)
        for i in self.edges:
            print '({}, {})'.format(i.x, i.y),
        print ''
        self.fused_nodes.extend(x.fused_nodes)
        self.fused_nodes.append(Vertex(x.x, x.y))
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
        for i in self.edges:
            print '({}, {})'.format(i.x, i.y),
        print ''
        print 'Done'


    def add_edge(self, n):
        if not n == self:
            self.edges.append(n)

    def __str__(self):
        str_tmp = []
        for i in self.edges:
            str_tmp.append('({},{})'.format(i.x, i.y))
        fused_tmp = []
        for i in self.fused_nodes:
            fused_tmp.append('({},{})'.format(i.x, i.y))
        return '[ ({},{}) : {str_tmp} : Fused Nodes: {fused_tmp} ]'.format(self.x, self.y, str_tmp = str_tmp, fused_tmp = fused_tmp)


def print_adj_list(adj_list):
    for node in adj_list:
        print node


def random_contraction(adj_list):
    if len(adj_list) <= 2:
        return
    pivot = choice(adj_list)
    x = choice(pivot.edges)
    print '--------'
    print 'Contracting {} and {}'.format(pivot, x)
    pivot.fuse(x)
    for i in range(len(adj_list)):
        if adj_list[i] == x:
            del adj_list[i]
            break
    print 'After Contraction'
    print_adj_list(adj_list)
    print '--------'
    if len(adj_list) > 2:
        random_contraction(adj_list)


if __name__ == '__main__':
    adj_list = []
    fd = open(sys.argv[1])
    for line in fd.readlines():
        line.strip('\n')
        (x1, y1, x2, y2) = line.split(',')
        a = Vertex(int(x1), int(y1))
        b = Vertex(int(x2), int(y2))
        a_found = False
        b_found = False
        for node in adj_list:
            if node == a:
                a = node
                a_found = True
            if node == b:
                b = node
                b_found = True
        if not a_found:
            adj_list.append(a)
        if not b_found:
            adj_list.append(b)
        b.add_edge(a)
        a.add_edge(b)
    print_adj_list(adj_list)
    random_contraction(adj_list)
    print_adj_list(adj_list)
