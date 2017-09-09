#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums = sorted(nums)
        for i in range(len(nums) - 2):
            if nums[i] <= 0 and (i==0 or nums[i-1]!=nums[i]):
                l = i + 1
                r = len(nums) - 1
                s = nums[i] + nums[l] + nums[r]
                while l < r:
                    if s < 0:
                        l += 1
                        s = nums[i] + nums[l] + nums[r]
                    elif s > 0:
                        r -= 1
                        s = nums[i] + nums[l] + nums[r]
                    elif s == 0:
                        result.append([nums[i], nums[l], nums[r]])
                        tmp = nums[l]
                        while l<r and nums[l] == tmp:
                            l += 1
                        s = nums[i] + nums[l] + nums[r]
            elif nums[i] >0:
                break

        return result


# print(Solution().threeSum([0,0,0]))
print(Solution().threeSum([-1,0,1,2,-1,-4]))
