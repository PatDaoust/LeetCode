# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 14:17:23 2021

@author: catal
"""

from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


print(twoSum([2,7,11,15], 9))
