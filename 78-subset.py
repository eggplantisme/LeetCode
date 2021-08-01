# 给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

# 说明：解集不能包含重复的子集。
class Solution:

    def subsets(self, nums):
        sets = []
        if len(nums) == 1:
            sets.append(nums)
            return sets
        else:
            for i in range()
