from typing import List

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))

        if len(nums) < 3:
            return max(nums)

        nums.remove(max(nums))
        nums.remove(max(nums))
        return max(nums)


solution_instance = Solution()
print(solution_instance.thirdMax([4,2,4,0,0,3,0,5,1,0]))   