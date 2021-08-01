# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序
class Solution:
    def moveZeroes(self, nums) -> None:
        for i in range(len(nums)):
            j = i
            if nums[j] != 0:
                while j > 0 and nums[j - 1] == 0:
                    nums[j], nums[j - 1] = nums[j - 1], nums[j]
                    j -= 1

nums = [0, 1, 0, 3, 12]
Solution().moveZeroes(nums)
print(nums)