from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for i in nums:
            result ^= i
        return result


solution_instance = Solution()
print(solution_instance.singleNumber([2,2,1]))
print(solution_instance.singleNumber([4,1,2,1,2]))
print(solution_instance.singleNumber([1]))