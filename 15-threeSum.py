# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。

# 注意：答案中不可以包含重复的三元组。
class Solution:
    def threeSum(self, nums):
        if len(nums) < 3:
            return []
        result = []
        nums = sorted(nums)
        for i in range(len(nums) - 2):
            if i > 0  and nums[i] == nums[i - 1]:
                continue
            elif nums[i] > 0:
                return result
            else:
                l = i + 1
                r = len(nums) - 1
                last_two_num = set()
                while l < r:
                    if nums[i] + nums[l] + nums[r] == 0 and (nums[l], nums[r]) not in last_two_num:
                        result.append([nums[i], nums[l], nums[r]])
                        last_two_num.add((nums[l], nums[r]))
                        l += 1
                        r -= 1
                    elif nums[i] + nums[l] + nums[r] > 0:
                        r -= 1
                    elif nums[i] + nums[l] + nums[r] < 0:
                        l += 1
                    else:
                        l += 1
                        r -= 1
        return result

    
print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))

