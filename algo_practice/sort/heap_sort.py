#!/usr/bin/env python
from math import floor


a = [5, 3, 6, 3, 1, 2]


def parent(node):
    if node % 2 == 0:
        return node / 2 - 1
    return int(floor(node / 2))


def children(node):
    return (node * 2 + 1, node * 2 + 2)


def swap(in_array, x, y):
    tmp = in_array[x]
    in_array[x] = in_array[y]
    in_array[y] = tmp


def heapify(in_array, count):
    print 'Before: {}'.format((in_array[0:count + 1]))
    if count == 0:
        return
    cur_parent = parent(count)

    if in_array[cur_parent] < in_array[count]:
        swap(in_array, cur_parent, count)
        heapify(in_array, cur_parent)

def readjust_heap(in_array, count):
    i = 0
    while True:
        (left, right) = children(i)
        if left > count:
            break
        elif right > count:
            swap_location = left
        elif in_array[left] > in_array[right]:
            swap_location = left
        else:
            swap_location = right
        if in_array[swap_location] > in_array[i]:
            swap(in_array, swap_location, i)
            i = swap_location
        else:
            break


def heap_sort(in_array):
    # Create a balanced heap
    for i in range(len(in_array)):
        heapify(in_array, i)
    # Remove elements from top
    for i in reversed(range(len(in_array))):
       # Swap first and last element
       swap(in_array, 0, i)
       readjust_heap(in_array, i - 1)
    return in_array


if __name__ == '__main__':
    print heap_sort(a)
