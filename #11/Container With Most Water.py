#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        i = 0
        j = len(height) - 1
        max_area = 0
        while i < j:
            if i < j and height[i] <= height[j]:
                while i < j and height[i] <= height[j]:
                    if self.cal(height, i, j) > max_area:
                        max_area = self.cal(height, i, j)
                    i += 1
                if i == j :
                    break
                if (i < j) and height[i] >= height[j] and self.cal(height, i, j) > max_area:
                    max_area = self.cal(height, i, j)

            if i < j and height[i] > height[j]:
                while i < j and height[i] > height[j]:
                    if self.cal(height, i, j) > max_area:
                        max_area = self.cal(height, i, j)
                    j -= 1
                if i == j:
                    break
                if (i < j) and height[i] <= height[j] and self.cal(height, i, j) > max_area:
                    max_area = self.cal(height, i, j)

        return max_area

    def cal(self, height, i, j):
        return (j - i) * min(height[i], height[j])


print(Solution().maxArea([1,1]))
