from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        merge = []
        i, j = 0, 0
        while i < m or j < n:
            if i == m:
                merge.extend(nums2[j:])
                break
            if j == n:
                merge.extend(nums1[i:])
                break
            if nums1[i] < nums2[j]:
                merge.append(nums1[i])
                i = i + 1
            else:
                merge.append(nums2[j])
                j = j + 1
        if (m + n) % 2 == 0:
            return (merge[int((m+n)/2) - 1] + merge[int((m+n)/2)]) / 2
        else:
            return float(merge[int((m+n-1)/2)])

solution = Solution()
nums1 = [1, 2]
nums2 = [3, 4]
print(solution.findMedianSortedArrays(nums1, nums2))