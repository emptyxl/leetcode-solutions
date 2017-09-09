#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        import re
        pattern = re.compile(r'^[^\d]*?(-?[\d]+)')
        match = re.match(pattern, str)
        if match:
            return int(match.group(1))
        else:
            return 0



print(Solution().myAtoi(' !@#-123dfaf231'))