#!/usr/bin/env python
import sys
from random import randint


def rselect(arr, l, r, p):
    if l >= r:
        return
    random_pivot = randint(l, r)
    arr[random_pivot], arr[l] = arr[l], arr[random_pivot] # Move the random pivot to the begining
    pivot = l
    i = l + 1 # splits < elements from > elements
    for j in range(i, r + 1): # j splits partitioned and un partitioned
        if arr[j] <= arr[pivot]:
            # Swap arr[j] arr[i]
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[pivot], arr[i - 1] = arr[i - 1], arr[pivot] # Move pivot to the center #
    if i - 1 == p:
        return
    if i - 1 > p and  i - 2 > l:
        return rselect(arr, l, i - 2, p)
    if i - 1 < p and r > i:
        return rselect(arr, i, r, p)


if __name__ == '__main__':
    fd = open(sys.argv[1])
    arr = []
    for line in fd.readlines():
        line = line.strip('\n')
        line = line.strip()
        arr.append(long(line))
    print 'Input: '
    #print arr
    position = int(sys.argv[2])
    rselect(arr, 0, len(arr) - 1, position)
    print 'Output: '
    print arr[position]
