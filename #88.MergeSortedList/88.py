from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> List[int]:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        tail = m + n - 1
        while m > 0 and n > 0:
            if (nums1[m - 1] > nums2[n - 1]):
                nums1[tail] = nums1[m - 1]
                m -= 1
            else:
                nums1[tail] = nums2[n - 1]
                n -= 1
            tail -= 1
        while n > 0:
            nums1[tail] = nums2[n - 1]
            n -= 1
            tail -= 1
        return nums1


solution = Solution()
print(solution.merge([1,2,3,0,0,0], 3, [2,5,6], 3))

