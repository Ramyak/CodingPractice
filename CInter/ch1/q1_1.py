#!/usr/bin/env python
import sys

# Implement an algorithm to determine if a string has all unique characters What if you can not use additional data structures?


def is_uniq_char_string(s):
    for i in range(len(s)):
        for j in range(i):
            if s[i] == s[j]:
                return False
    return True


if __name__ == '__main__':
    print is_uniq_char_string(sys.argv[1])
