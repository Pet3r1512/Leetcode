from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        r = []

        for i in nums1:
            r.append(-1)
            index = nums2.index(i)
            if index != len(nums2) - 1:
                for k in range(index + 1, len(nums2)):
                    if nums2[k] > i:
                        r.pop()
                        r.append(nums2[k])
                        break
                    
        return r 


solution_instance = Solution()
print(solution_instance.nextGreaterElement([4, 1, 2], [1, 3, 4, 2])) 