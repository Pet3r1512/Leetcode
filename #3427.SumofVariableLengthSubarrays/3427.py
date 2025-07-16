from typing import List


class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        s = 0

        for i in range(len(nums)):
            s += sum(nums[max(0, i - nums[i]) : i + 1])

        return s

solution_instance = Solution()
print(solution_instance.subarraySum([2,3,1])) 
print(solution_instance.subarraySum([3,1,1,2]))