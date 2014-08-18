#!/usr/bin/env python


a = [5, 3, 6, 3, 1, 2]

def selection_sort(in_array):
    for i in range(len(in_array)):
        smallest_location = i
        for j in range(i + 1, len(in_array)):
            if in_array[j] < in_array[smallest_location]:
                smallest_location = j
        # Swap
        x = in_array[i]
        in_array[i] = in_array[smallest_location]
        in_array[smallest_location] = x
    return in_array
                

if __name__ == '__main__':
    print selection_sort(a)
