#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        result = ''
        for i in len(s):
            if len(self.search_pal(s, i, i)) > len(result):
                result = self.search_pal(s, i, i)
            if len(self.search_pal(s, i, i + 1)) > len(result):
                result = self.search_pal(s, i, i + 1)

        return result

    def search_pal(self, s, left, right):
        l = left
        r = right
        while l >= 0 and r < len(s):
            if s[l] == s[r]:
                l -= 1
                r += 1
            else:
                break
        return s[l + 1: r]
