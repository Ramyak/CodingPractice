#!/usr/bin/env python
import sys
from heapq import heappush, heappop

maxq_left = [] # negatives #
minq_right = []

def get_median(x):
    if len(minq_right) and x > minq_right[0]:
        heappush(minq_right, x)
        if len(minq_right) - 1 > len(maxq_left):
            heappush(maxq_left, - heappop(minq_right))
    else:
        heappush(maxq_left, -x)
        if len(maxq_left) - 1 > len(minq_right):
            heappush(minq_right, -heappop(maxq_left))
    if len(maxq_left) < len(minq_right):
        heappush(maxq_left, -heappop(minq_right))
    return -maxq_left[0]



def main_1():
    fd = open(sys.argv[1])
    mk_sum = 0
    for line in fd:
        no = int(line.strip('\n').strip())
        median = get_median(no)
        mk_sum += median
        #print maxq_left
        #print minq_right
        #print 'Median: {}'.format(median)
        #print '==========='
    print 'Result : {}'.format(mk_sum % 10000)

if __name__ == '__main__':
    #import cProfile
    #cProfile.runctx('main_1()', None, locals())
    main_1()
