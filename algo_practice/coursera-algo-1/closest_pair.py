#!/usr/bin/env python

arr = [(8, 3), (4, 8), (5, 7), (3, 1), (1, 5), (2, 2)]


class PointPair(object):
    def __init__(self, a, b):
        self.distance = ((b[1] - a[1]) ** 2 + (b[0]  - a[0]) ** 2) ** .5
        self.a = a
        self.b = b



def sort_arr(arr, index):
    if len(arr) <= 1:
        return arr

    middle = len(arr) / 2
    left_arr = sort_arr(arr[:middle], index)
    right_arr = sort_arr(arr[middle:], index)
    merged_arr = []
    for i in range(len(arr)):
        if len(left_arr) == 0 or len(right_arr) == 0:
            break
        if right_arr[0][index] < left_arr[0][index]:
            merged_arr.append(right_arr.pop(0))
        else:
            merged_arr.append(left_arr.pop(0))
    if len(left_arr):
        merged_arr.extend(left_arr)
    if len(right_arr):
        merged_arr.extend(right_arr)
    return merged_arr


sorted_x = sort_arr(arr, 0)
sorted_y = sort_arr(arr, 1)

def closest_pair(arr):
    if len(arr) == 2:
        return PointPair(arr[0], arr[1])
    if len(arr) == 3:
        p1 = PointPair(arr[0], arr[1])
        p2 = PointPair(arr[1], arr[2])
        return p1 if p1.distance < p2.distance else p2
    if len(arr) < 2:
        return None
    mid = len(arr) / 2
    left_closest_pair = closest_pair(arr[:mid])
    right_closest_pair = closest_pair(arr[mid:])
    best_closest_pair = left_closest_pair
    if best_closest_pair and right_closest_pair and \
            best_closest_pair.distance > right_closest_pair.distance:
                best_closest_pair = right_closest_pair
    if best_closest_pair:
        xmedian  = arr[len(arr)/2]
        s_unsorted = []
        for point in arr:
            if  xmedian[0] - best_closest_pair.distance <= point[0] <= xmedian[0] or \
                    xmedian[0] < point[0] <= xmedian[0] + best_closest_pair.distance:
                        s_unsorted.append(point)
        s_sorted = []
        for point in sorted_y:
            for spoint in s_unsorted:
                if spoint[0] == point[0] and spoint[1] == point[1]:
                    s_sorted.append(spoint)
        for i in range(len(s_sorted) - 7):
            for compare_point in s_sorted[i + 1: i + 8]:
                new_point_pair = PointPair(s_sorted[i], compare_point)
                if new_point_pair.distance < best_closest_pair.distance:
                    new_point_pair = best_closest_pair
    return best_closest_pair


if __name__ == '__main__':
    print 'Input: '
    print arr
    best_closest_pair = closest_pair(sorted_x)
    if best_closest_pair:
        print best_closest_pair.a
        print best_closest_pair.b
        print best_closest_pair.distance



