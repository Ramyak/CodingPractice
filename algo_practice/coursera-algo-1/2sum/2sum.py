#!/usr/bin/env python
import sys

hash_arr = {}
arr = []


debug = False
#debug = True

def read_hash():
    fd = open(sys.argv[1])
    i = 0
    for line in fd:
        no = int(line.strip('\n').strip())
        arr.append(no)
        if no in hash_arr:
            hash_arr[no].append(i)
        else:
            hash_arr[no] = [i]
        i += 1

def print_hash():
    for no in arr:
        print '{}:{}'.format(no, hash_arr[no])

def find_pair_given_position(t):
    print 't: {} '.format(t)
    for ax in range(len(arr)):
        a = arr[ax]
        b = t - a
        if a >= t or a == b:
            continue
        if b in hash_arr:
            if hash_arr[b][-1] > ax:
                if debug:
                    print (a, b)
                return True
    return False


def count_pairs_range(x, y):
    cnt = 0
    for i in range(x, y + 1):
        if find_pair_given_position(i):
            cnt += 1
    print 'grand total = {}'.format(cnt)

def main_1():
    print 'Reading hash'
    read_hash()
    print 'Read hash'
    if debug:
        print arr
    count_pairs_range(int(sys.argv[2]), int(sys.argv[3]))


if __name__ == '__main__':
    import cProfile
    cProfile.runctx('main_1()', None, locals())

