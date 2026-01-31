from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for k, v in enumerate(nums):
            completion = target - v

            if completion in seen:
                return [seen[completion], k]

            seen[v] = k

solution_instance = Solution()

print(solution_instance.twoSum([2,7,11,15], 9))
print(solution_instance.twoSum([3, 2, 4], 6))