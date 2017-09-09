#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        a = []
        for i in range(numRows):
            a.append('')
        step = 2 * numRows - 2
        if numRows ==1:
            return s
        elif numRows > 0:
            for i in range(0, len(s)):
                if i % step == 0:
                    a[0] += s[i]
                elif i % step <= numRows - 1:
                    a[i % step] += s[i]
                else:
                    a[step - i % step] += s[i]
        result = ''
        for i in range(numRows):
            result += a[i]
        return result


print(Solution().convert('A', 1))
