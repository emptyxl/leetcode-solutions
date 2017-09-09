#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max = 0
        i = -1
        string = ''
        while i < len(s) - 1:
            i += 1
            if string.find(s[i]):
                string += s[i]
                string = string[string.find(s[i]) + 1 : i + 1]
            else:
                string += s[i]
            if len(string) > max:
                max = len(string)
        return max
