#!/usr/bin/env python


a = [5, 3, 6, 3, 1, 2]

def merge_sort(in_array, left, right):
    print 'Before: ({} , {}) : {}'.format(str(left), str(right), (in_array[left:right + 1]))
    if right - left >= 1:
        mid = ((right - left) / 2) + left
        if mid > right:
            return
        merge_sort(in_array, left, mid)
        merge_sort(in_array, mid + 1, right)
        # Merge
        tmp_array = [None] * (right - left + 1)
        l_start = left
        r_start = mid + 1
        i = 0
        for i in range(right + 1 - left):
            if l_start > mid or r_start > right:
                break
            if in_array[l_start] < in_array[r_start]:
                tmp_array[i] = in_array[l_start]
                l_start += 1
            else:
                tmp_array[i] = in_array[r_start]
                r_start += 1
        if l_start <= mid:
            tmp_array[i:right + 1] = in_array[l_start:mid + 1]
        else:
            tmp_array[i:right + 1] = in_array[r_start:right + 1]
        in_array[left:right + 1] = tmp_array
    print 'After: ({} , {}) : {}'.format(str(left), str(right), (in_array[left:right + 1]))
    return in_array

            

if __name__ == '__main__':
    print merge_sort(a, 0, len(a) - 1)
