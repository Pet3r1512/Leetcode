from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1 and nums[0] == 0:
            return [0]
        
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] == 0 and nums[j] != 0:
                    temp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = temp
        return nums

solution_instance = Solution()
print(solution_instance.moveZeroes([4,2,4,0,0,3,0,5,1,0]))  
print(solution_instance.moveZeroes([0,1,0,3,12]))  