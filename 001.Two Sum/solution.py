#coding=utf-8


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        set = {}
        for index, val in enumerate(nums):
            m = target - val
            if m in set:
                return [nums.index(m), index]
            set[val] = index