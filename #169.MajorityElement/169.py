from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        eSet = dict()

        flag = len(nums)/2

        if len(nums) == 1:
            return nums[0]

        for i in nums:
            if i not in eSet:
                eSet[i] = 1
            else:
                eSet[i] += 1
        print(eSet)

        for s in eSet:
            if eSet.get(s) > flag:
                return s

solution_instance = Solution()
print(solution_instance.majorityElement([6, 5, 5]))