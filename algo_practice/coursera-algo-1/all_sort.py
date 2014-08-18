#!/usr/bin/env python

arr = [64, 25, 12, 22, 11]


def selection_sort(arr, i):
    if i == (len(arr) - 1): 
        # Last element
        return
    # Find smallest element #
    smallest_pos = i
    for j in range(i, len(arr)):
        if arr[smallest_pos] > arr[j]:
            smallest_pos = j
    if smallest_pos != i:
        # swap
        arr[smallest_pos], arr[i] = arr[i], arr[smallest_pos]
    selection_sort(arr, i + 1)


def insertion_sort(arr, i):
    if i == len(arr):
        # Past last element
        return
    for j in range(i):
        if arr[j] > arr[i]:
            arr[j:j] = [arr[i]]
            del arr[i + 1]
            print 'After a swap'
            print arr
            break
    insertion_sort(arr, i + 1)

def bubble_sort(arr):
    any_misses = False
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            any_misses = True
    if any_misses:
        bubble_sort(arr)

def merge_sort_1(arr, left, right):
    if right - left <= 1:
        if arr[left] > arr[right]:
            arr[left], arr[right] = arr[right], arr[left]
        return arr[left:right + 1]
    middle = (left + right) / 2
    left_arr = merge_sort(arr, left, middle)
    right_arr = merge_sort(arr, middle + 1, right)
    result = []
    left_index = right_index = 0
    print '2 groups'
    print left_arr
    print right_arr
    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] > right_arr[right_index]:
            result.append(right_arr[right_index])
            right_index += 1
        else:
            result.append(left_arr[left_index])
            left_index += 1
    if left_index == len(left_arr):
        result.extend(right_arr[right_index:])
    else:
        result.extend(left_arr[left_index:])

    print 'result'
    print result
    return result

def merge_sort(arr, left, right):
    if left >= right:
        return arr[left:left + 1]
    middle = (left + right) / 2
    left_arr = merge_sort(arr, left, middle)
    right_arr = merge_sort(arr, middle + 1, right)
    result = []
    left_index = right_index = 0
    print '2 groups'
    print left_arr
    print right_arr
    for i in range(right - left + 1):
        if left_index == len(left_arr):
            result.extend(right_arr[right_index:])
            break
        if right_index == len(right_arr):
            result.extend(left_arr[left_index:])
            break
        if left_arr[left_index] > right_arr[right_index]:
            result.append(right_arr[right_index])
            right_index += 1
        else:
            result.append(left_arr[left_index])
            left_index += 1
    print 'result'
    print result
    return result


print arr
print '-----------'
#selection_sort(arr, 0)
#insertion_sort(arr, 0)
merge_sort(arr, 0, len(arr) - 1)
print '-----------'
print arr

