#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        return str(x) == str(x)[::-1]
