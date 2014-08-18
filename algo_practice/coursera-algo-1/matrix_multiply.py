#!/usr/bin/env python

arr1 = [(1, 2, 3, 4),
        (5, 6, 7, 8),
        (9, 10, 11, 12),
        (13, 14, 15, 16),
        ]

arr2 = [(1, 2, 3, 4),
        (5, 6, 7, 8),
        (9, 10, 11, 12),
        (13, 14, 15, 17),
        ]


def print_arr(arr1, arr2 = None):
    print '----------------'
    if not arr1 or len(arr1) == 0:
        return
    for i in range(len(arr1)):
        line_str = '\t'.join([str(x) for x in arr1[i]])
        if arr2 and len(arr2):
            if i == len(arr1)/2:
                line_str = '{}\t*\t'.format(line_str)
            else:
                line_str = line_str + '\t\t'
            line_str = line_str + '\t'.join([str(x) for x in arr2[i]])
        print line_str
    print '----------------'

def divide_four(arr):
    mid = len(arr)/2
    A = []
    B = []
    C = []
    D = []
    for line in arr[:mid]:
        A.append(line[:mid])
        B.append(line[mid:])
    for line in arr[mid:]:
        C.append(line[:mid])
        D.append(line[mid:])
    return (A, B, C, D)

def add(arr1, arr2):
    result = []
    for i in range(len(arr1)):
        result.append([0] * len(arr1))
    for i in range(len(arr1)):
        for j in range(len(arr1[i])):
            result[i][j] = arr1[i][j] + arr2[i][j]
    return result


def join_four(A, B, C, D):
    result = []
    for i in range(len(A)):
        line = []
        line.extend(A[i])
        line.extend(B[i])
        result.append(line)
    for i in range(len(C)):
        line = []
        line.extend(C[i])
        line.extend(D[i])
        result.append(line)
    return result

'''
A, B   *   E, F
C, D   *   G, H

AE + BG      AF + BH
CE + DG      CF + DH

'''

def multiply (arr1, arr2):
    if len(arr1) == 1:
        return [[arr1[0][0] * arr2[0][0]],]
    mid = len(arr1)/2
    (A, B, C, D) = divide_four(arr1)
    (E, F, G, H) = divide_four(arr2)
    AE = multiply(A, E)
    BG = multiply(B, G)
    CE = multiply(C, E)
    DG = multiply(D, G)
    AF = multiply(A, F)
    BH = multiply(B, H)
    CF = multiply(C, F)
    DH = multiply(D, H)
    a = add(AE, BG)
    b = add(AF, BH)
    c = add(CE, DG)
    d = add(CF, DH)
    result = join_four(a, b, c, d)
    return result




if __name__ == '__main__':
    print 'Input: '
    print_arr(arr1, arr2)
    result_arr = multiply(arr1, arr2)
    print 'Output: '
    print_arr(result_arr)


