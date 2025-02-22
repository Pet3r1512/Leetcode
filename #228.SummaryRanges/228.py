from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        i = 0
        while i < len(nums):
            s = nums[i]
            while i + 1 < len(nums) and nums[i] + 1 == nums[i + 1]:
                i += 1

            if s == nums[i]:
                result.append(str(s))
            else:
                result.append(str(s) + "->" + str(nums[i]))
            i += 1
        return result



solution_instance = Solution()
print(solution_instance.summaryRanges([0,1,2,4,5,7])) 