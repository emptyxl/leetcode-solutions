#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        dp = []
        for i in range(len(s) + 1):
            dp.append([False] * (len(p) + 1))
        dp[0][0] = True

        for i in range(len(s)):
            for j in range(len(p)):
                if dp[i][j]:
                    if p[j] == '*' and j - 1 >= 0 and i + 1 < len(s) and (p[j - 1] == s[i + 1] or p[j - 1] == '.'):
                        dp[i + 1][j] = True
                    if p[j] != '*' and j + 1 < len(p) and p[j + 1] == '*':
                        dp[i][j + 1] = True
                    if j + 2 < len(p) and p[j + 2] == '*':
                        dp[i][j + 2] = True
                    if i + 1 < len(s) and j + 1 < len(p):
                        if p[j + 1] == '.' or p[j + 1] == s[i + 1]:
                            dp[i + 1][j + 1] = True
        print(dp)
        return dp[len(s) - 1][len(p) - 1]


print(Solution().isMatch('ab', '.*..'))
