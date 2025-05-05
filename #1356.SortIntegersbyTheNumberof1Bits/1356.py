from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key=lambda x : (str(bin(x)).count("1"), x))

solution_instance = Solution()
print(solution_instance.sortByBits([0,1,2,3,4,5,6,7,8]))  
print(solution_instance.sortByBits([1024,512,256,128,64,32,16,8,4,2,1]))