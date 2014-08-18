#!/usr/bin/env python
import sys
from random import randint
cnt = 0


def quick_sort(arr, l, r):
    global cnt
    cnt = cnt + (r - l)
    if l >= r:
        return
    middle = (r - l) / 2 + l
    x = [-1, -1, -1]
    if arr[l] > arr[middle]:
        x[0], x[2] = middle, l
    else:
        x[0], x[2] = l, middle
    if arr[r] > arr[x[0]]:
        if arr[r] > arr[x[2]]:
            x[1], x[2] = x[2], r
        else:
            x[1] = r
    else:
        x[0], x[1] = r, x[0]
    median = x[1]
    arr[median], arr[l] = arr[l], arr[median] # Move the random pivot to the begining
    pivot = l
    i = l + 1 # splits < elements from > elements
    for j in range(i, r + 1): # j splits partitioned and un partitioned
        if arr[j] <= arr[pivot]:
            # Swap arr[j] arr[i]
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[pivot], arr[i - 1] = arr[i - 1], arr[pivot] # Move pivot to the center #
    if i - 2 > l:
        quick_sort(arr, l, i - 2)
    if r > i:
        quick_sort(arr, i, r)


if __name__ == '__main__':
    fd = open(sys.argv[1])
    arr = []
    for line in fd.readlines():
        line = line.strip('\n')
        line = line.strip()
        arr.append(long(line))
    print 'Input: '
    #print arr
    quick_sort(arr, 0, len(arr) - 1)
    print 'Output: '
    print cnt
    for i in arr:
         print i
