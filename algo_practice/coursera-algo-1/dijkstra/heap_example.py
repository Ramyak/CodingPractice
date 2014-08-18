#!/usr/bin/env python
from heap import Heap

left_heap = Heap(is_min = False)
right_heap = Heap()

def add_get_median(x):
    if len(right_heap.arr) and x > right_heap.arr[0]:
        right_heap.add(x)
    else:
        left_heap.add(x)
    if abs(len(right_heap.arr) - len(left_heap.arr)) > 1:
        if len(right_heap.arr) > len(left_heap.arr):
            left_heap.add(right_heap.get())
        else:
            right_heap.add(left_heap.get())
    a = [left_heap.arr[0]]
    if len(right_heap.arr):
        a.append(right_heap.arr[0])
    print 'Media: {}'.format(a)

def median_wrapper():
    a = [53, 19, 8, 56, 4, 91, 92, 76, 88, 19, 19, 37, 83, 60, 14, 32, 68, 22, 59, 3, 13, 81, 35, 88, 55, 42, 18, 21, 96, 58, 39, 59, 25, 26, 34, 4, 76, 25, 59, 66, 56, 58, 13, 85, 25, 48, 9, 62, 47, 16, 0, 96, 54, 82, 77, 86, 13, 59, 86, 43, 86, 39, 56, 79, 76, 57, 69, 5, 91, 31, 68, 67, 32, 45, 86, 40, 17, 85, 89, 78, 83, 46, 22, 85, 11, 57, 14, 40, 91, 87, 79, 52, 64, 68, 14, 72, 100, 8, 99, 76]
    for i in a:
        add_get_median(i)

def sort():
    a = [53, 19, 8, 56, 4, 91, 92, 76, 88, 19, 19, 37, 83, 60, 14, 32, 68, 22, 59, 3, 13, 81, 35, 88, 55, 42, 18, 21, 96, 58, 39, 59, 25, 26, 34, 4, 76, 25, 59, 66, 56, 58, 13, 85, 25, 48, 9, 62, 47, 16, 0, 96, 54, 82, 77, 86, 13, 59, 86, 43, 86, 39, 56, 79, 76, 57, 69, 5, 91, 31, 68, 67, 32, 45, 86, 40, 17, 85, 89, 78, 83, 46, 22, 85, 11, 57, 14, 40, 91, 87, 79, 52, 64, 68, 14, 72, 100, 8, 99, 76]
    h = Heap(is_min = True)
    for i in a:
        h.add(i)
    sorted_arr = []
    while True:
        i = h.get()
        if i == None:
            break
        sorted_arr.append(i)
    print 'Input'
    print a
    print 'Sorted output'
    print sorted_arr

def sort_del():
    a = [53, 19, 8, 56, 4, 91, 92, 76, 88, 19, 19, 37, 83, 60, 14, 32, 68, 22, 59,]
    h = Heap(is_min = True)
    for i in a:
        x = h.add(i)
        print 'Added {} at {}'.format(i, x)
        print h.arr
    sorted_arr = []
    print 'Deleting node {}'.format(h.arr[0])
    h.del_node(0)
    print 'Deleting node {}'.format(h.arr[0])
    h.del_node(0)
    while True:
        i = h.get()
        if i == None:
            break
        sorted_arr.append(i)
    print 'Input'
    print a
    print 'Sorted output'
    print sorted_arr


if __name__ == '__main__':
    sort_del()
