from typing import List


class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        r = []

        for i in range(len(nums)):
            prefix = nums[0: i + 1]
            distinct_prefix = len(set(prefix))
            suffix = nums[i + 1: len(nums)]
            distinct_suffix = len(set(suffix))
            r.append(distinct_prefix - distinct_suffix)

        return r

solution_instance = Solution()
print(solution_instance.distinctDifferenceArray([1,2,3,4,5]))  
print(solution_instance.distinctDifferenceArray([3,2,3,4,2]))