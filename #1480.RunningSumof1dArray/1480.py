from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        r = []
        r.append(nums[0])
        for i in range(1, len(nums)):
            r.append(nums[i] + r[i - 1])  

        return r

solution_instance = Solution()
print(solution_instance.runningSum([1,2,3,4])) 