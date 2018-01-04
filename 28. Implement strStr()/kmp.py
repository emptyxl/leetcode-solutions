#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# KMP Algorithm


def search_string(string, pattern, next):
    sLen = len(string)
    pLen = len(pattern)

    i = 0
    j = 0

    if sLen <= 0 or pLen <= 0:
        return -1

    while (i < sLen and j < pLen):
        if (j == -1 or string[i] == pattern[j]):
            i += 1
            j += 1
            if j == pLen:
                return i - j
        else:
            j = next[j]

    return -1


def create_next(pattern):

    next = list((0 for i in range(len(pattern))))

    if len(pattern) == 0:
        return next
    else:
        next[0] = -1
        if len(pattern) <= 2:
            return next
        else:
            for i in range(2, len(pattern)):
                lchar = pattern[next[i - 1]]
                rchar = pattern[i - 1]
                if lchar == rchar:
                    next[i] = next[i - 1] + 1
                else:
                    k = next[i - 1]
                    while (k != -1 and pattern[k] != rchar):
                        k = next[k]
                    next[i] = k + 1
            return next


def main():
    original_string = input()
    pattern = input()
    next = create_next(pattern)
    index = search_string(original_string, pattern, next)
    print(index)


if __name__ == '__main__':
    main()
