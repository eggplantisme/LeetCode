# 给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。
# 假设只有一个重复的整数，找出这个重复的数。
class Solution:
    def findDuplicate(self, nums) -> int:
        for i in range(len(nums)):
            if nums[i] in nums[:i]:
                return nums[i]

print(Solution().findDuplicate([1, 3, 3, 4, 2]))