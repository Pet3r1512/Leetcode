from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count repeat elements in nums
        d = dict(Counter(nums).items())
        # sort the dictionary by values (repeat times)
        d = dict(sorted(d.items(), key=lambda item: item[1]))
        # store in an array an retrun last K elements
        return [k for k in d.keys()][-k:]
    
solution_instance = Solution()
print(solution_instance.topKFrequent([1,1,1,2,2,3], 2))  
print(solution_instance.topKFrequent([1], 1))