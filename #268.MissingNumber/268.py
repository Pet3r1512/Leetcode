from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()

        for i in range(len(nums) + 1):
            if i not in nums:
                return i
                
solution_instance = Solution()
print(solution_instance.missingNumber([9,6,4,2,3,5,7,0,1]))  
print(solution_instance.missingNumber([3,0,1]))  