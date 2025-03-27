from typing import List


class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        d = dict()

        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = i
            else:
                d[s[i]] = i - d[s[i]] - 1
                
        for i in range(len(distance)):
            letter = chr(ord('a') + i)
            if letter in d and d[letter] != distance[i]:
                return False
            
        return True
        

solution_instance = Solution()
print(solution_instance.checkDistances("abaccb", [1,3,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]))  
print(solution_instance.checkDistances("aa", [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]))  