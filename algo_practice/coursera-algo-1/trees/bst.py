#!/usr/bin/env python
from random import randint

class Node:
    def __init__(self, x):
        self.x = x
        self.parent = None
        self.left = None
        self.right = None
        self.size = 1

class Btree:
    def add(self, x, node):
        node.size += 1
        if node.x > x:
            if node.left == None:
                node.left = Node(x)
                node.left.parent = node
            else:
                self.add(x, node.left)
        else:
            if node.right == None:
                node.right = Node(x)
                node.right.parent = node
            else:
                self.add(x, node.right)
    def sorted_arr(self, node):
        arr = []
        if node.left:
            arr.extend(self.sorted_arr(node.left))
        arr.append(node.x)
        if node.right:
            arr.extend(self.sorted_arr(node.right))
        return arr
        
    def min(self, node):
        if node.left == None:
            return node
        else:
            return self.min(node.left)
    def max(self, node):
        if node.right == None:
            return node
        else:
            return self.max(node.right)
    def predecessor(self, x, node):
        if node.x == x:
            if node.left != None:
                return self.max(node.left).x
            else:
                p = node.parent
                while p.x > x and p.parent != None:
                    p = p.parent
                return p.x
        elif node.x > x:
            return self.predecessor(x, node.left)
        else:
            return self.predecessor(x, node.right)
    def successor(self, x, node):
        if node.x == x:
            if node.right != None:
                return self.min(node.right).x
            else:
                p = node.parent
                while p.x < x and p.parent != None:
                    p = p.parent
                return p.x
        elif node.x > x:
            return self.successor(x, node.left)
        else:
            return self.successor(x, node.right)

    def select(self, x, node):
        if x == node.size:
            return node.x
        elif node.left == None and x == 0:
            return node.x
        elif (node.left and node.left.size >= x):
            return self.select(x, node.left)
        elif node.right:
            mod_size = (x - node.left.size - 1) \
                    if node.left else (x - 1)
            return self.select(mod_size, node.right)
        else:
            print 'err'
            return -1
    def rank(self, x, node, adds = 0):
        if x == node.x:
            if node.left:
                adds += node.left.size
            return adds
        elif x < node.x:
            return self.rank(x, node.left, adds)
        else:
            adds += 1
            if node.left:
                adds += node.left.size
            return self.rank(x, node.right, adds)
    def delete(self, x, node):
        while x != node.x:
            if node.x < x:
                node = node.right
            else:
                node = node.left
        if node.left == None or node.right == None:
            child = node.left if node.left else node.right
            if node.parent.left == node:
                node.parent.left = child
            else:
                node.parent.right = child
            print 'Deleted node {}'.format(node.x)
            return
        else:
            print 'Deleted node {}'.format(node.x)
            neigh = self.max(node.left)
            node.x = neigh.x
            if neigh.parent.left == neigh:
                neigh.parent.left = None
            else:
                neigh.parent.right = None
            neigh.parent = None





def operations():
    root = Node(randint(0, 100))
    btree = Btree()
    '''
    for i in range(100 - 1):
        btree.add(randint(0, 100), root)
    '''
    a = [53, 19, 8, 56, 4, 91, 92, 76, 88, 19, 19, 37, 83, 60, 14, 32, 68, 22, 59, 3, 13, 81, 35, 88, 55, 42, 18, 21, 96, 58, 39, 59, 25, 26, 34, 4, 76, 25, 59, 66, 56, 58, 13, 85, 25, 48, 9, 62, 47, 16, 0, 96, 54, 82, 77, 86, 13, 59, 86, 43, 86, 39, 56, 79, 76, 57, 69, 5, 91, 31, 68, 67, 32, 45, 86, 40, 17, 85, 89, 78, 83, 46, 22, 85, 11, 57, 14, 40, 91, 87, 79, 52, 64, 68, 14, 72, 100, 8, 99, 76]
    for i in a:
        btree.add(i, root)
    print 'Sorted arr : {}'.format(btree.sorted_arr(root))
    btree.delete(76, root)
    btree.delete(100, root)
    btree.delete(4, root)
    print 'Sorted arr : {}'.format(btree.sorted_arr(root))
    print 'Min {}'.format(btree.min(root).x)
    print 'Max {}'.format(btree.max(root).x)
    x = 56
    print 'Predecessor of {} is {}'.format(x, btree.predecessor(x, root))
    x = 4
    print 'Predecessor of {} is {}'.format(x, btree.predecessor(x, root))
    x = 17
    print 'Predecessor of {} is {}'.format(x, btree.predecessor(x, root))
    x = 56
    print 'Successor of {} is {}'.format(x, btree.successor(x, root))
    x = 4
    print 'Successor of {} is {}'.format(x, btree.successor(x, root))
    x = 31
    print 'Successor of {} is {}'.format(x, btree.successor(x, root))
    x = 1
    print 'Select of {} is {}'.format(x, btree.select(x, root))
    x = 30
    print 'Select of {} is {}'.format(x, btree.select(x, root))
    x = 40
    print 'Select of {} is {}'.format(x, btree.select(x, root))
    x = 0
    print 'Select of {} is {}'.format(x, btree.select(x, root))
    x = 50
    print 'Select of {} is {}'.format(x, btree.select(x, root))
    x = 99
    print 'Select of {} is {}'.format(x, btree.select(x, root))
    x = 99
    print 'Rank of {} is {}'.format(x, btree.rank(x, root))
    x = 8
    print 'Rank of {} is {}'.format(x, btree.rank(x, root))
    x = 91
    print 'Rank of {} is {}'.format(x, btree.rank(x, root))



def operations_2():
    a = [53, 19, 8, 56, 4, 91, 92, 52]
    root = Node(51)
    #root = Node(randint(0, 100))
    btree = Btree()
    for i in a:
        btree.add(i, root)
    print 'Sorted arr : {}'.format(btree.sorted_arr(root))

if __name__ == '__main__':
    operations()
    #operations_2()
