from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        
        if len(nums1) < len(nums2):
            for i in nums1:
                if i in nums2 and i not in result:
                    result.append(i)

        else:
            for i in nums2:
                if i in nums1 and i not in result:
                    result.append(i)

        return result

 
solution_instance = Solution()
print(solution_instance.intersection([4,2,4,0,0,3,0,5,1,0], [2,4,0]))        