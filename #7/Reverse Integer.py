#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        v = int(str(abs(x))[::-1])
        v = v if v <= (1 << 31) - 1 else 0
        return v if x >= 0 else int('-' + str(v))
