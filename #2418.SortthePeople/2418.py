from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        d = dict()

        for i in range(len(names)):
            d[heights[i]] = names[i]
        
        heights.sort(reverse=True)
        r = []

        for h in heights:
            r.append(d[h])

        return r
        
solution_instance = Solution()
print(solution_instance.sortPeople(["Mary","John","Emma"], [180,165,170]))  
print(solution_instance.sortPeople(["Alice","Bob","Bob"], [155,185,150]))  