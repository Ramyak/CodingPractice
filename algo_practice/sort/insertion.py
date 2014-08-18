#!/usr/bin/env python


a = [5, 3, 6, 3, 1, 2]

def insertion_sort(in_array):
    s_array = [None] * len(in_array)
    for i in range(len(s_array)):
        smallest_location = 0
        for j in range(len(in_array)):
            if in_array[j] < in_array[smallest_location]:
                smallest_location = j
        s_array[i] = in_array[smallest_location]
        del in_array[smallest_location]
    return s_array
                
        
        



if __name__ == '__main__':
    print insertion_sort(a)
