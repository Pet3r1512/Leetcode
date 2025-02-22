from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        got = set()

        for i in range(len(nums)):
            if nums[i] in got:
                return True

            got.add(nums[i])
            
            if len(got) > k:
                got.remove(nums[i - k])

        return False


solution_instance = Solution()
print(solution_instance.containsNearbyDuplicate([1,2,3,1,2,3], 2))  