#!/usr/bin/env python
import sys
#arr = [64, 25, 12, 22, 11]


def split_inversion(arr):
    if len(arr) <= 1:
        return (0, arr)

    middle = len(arr) / 2
    (left_count, left_arr) = split_inversion(arr[:middle])
    (right_count, right_arr) = split_inversion(arr[middle:len(arr)])
    total_count = left_count + right_count
    merged_arr = []

    for i in range(len(arr)):
        if len(left_arr) == 0 or len(right_arr) == 0:
            break
        if right_arr[0] < left_arr[0]:
            merged_arr.append(right_arr.pop(0))
            total_count += len(left_arr)
        else:
            merged_arr.append(left_arr.pop(0))
    if len(left_arr):
        merged_arr.extend(left_arr)
    if len(right_arr):
        merged_arr.extend(right_arr)
    return (total_count, merged_arr)


if __name__ == '__main__':
    fd = open(sys.argv[1])
    arr = []
    for line in fd.readlines():
        line = line.strip('\n')
        line = line.strip()
        arr.append(long(line))
    print 'Input: '
    (total_count, merged_arr) = split_inversion(arr)
    print 'Output: '
    #print merged_arr
    print total_count




    

