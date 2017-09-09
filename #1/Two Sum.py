#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    map = {}
    for i in range(len(nums)):
    	if nums[i] not in map:
    		map[target - nums[i]] = i
    	else:
    		return [map[nums[i]],i]


