from typing import List


class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        nums.sort(reverse=True)
        idx = 0
        for i in range(len(nums) - 1):
            if nums[i] < 10:
                idx = i - 1
                break
        
        return sum(nums[:idx + 1]) != sum(nums[idx + 1:])

solution_instance = Solution()
print(solution_instance.canAliceWin([1,2,3,4,10]))  
print(solution_instance.canAliceWin([1,2,3,4,5,14]))
print(solution_instance.canAliceWin([5,5,5,25]))