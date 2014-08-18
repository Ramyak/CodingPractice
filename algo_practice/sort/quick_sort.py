#!/usr/bin/env python
from math import floor


a = [5, 3, 6, 3, 1, 2]


def quick_sort(in_array, left, right):
    print 'Before ({}, {}): {}'.format(left, right, in_array[left: right + 1])
    if left >= right:
        return
    pivot = left
    for i in range(left + 1, right + 1):
        if in_array[i] <= in_array[pivot]:
            x = in_array[i]
            in_array[pivot + 1: i + 1] = in_array[pivot: i]
            in_array[pivot] = x
            pivot += 1
            continue
    quick_sort(in_array, left, pivot - 1)
    quick_sort(in_array, pivot + 1, right)
    print 'After ({}, {}): {}'.format(left, right, in_array[left: right + 1])
    return in_array
 


if __name__ == '__main__':
    print quick_sort(a, 0, len(a) - 1)
