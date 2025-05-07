from typing import List


class Solution:
    def captureForts(self, forts: List[int]) -> int:
        r, i = 0, 0

        while i < len(forts) - 1:
            if forts[i] == 1:
                for j in range(i + 1, len(forts)):
                    if forts[j] == -1:
                        if all(f == 0 for f in forts[i + 1: j]):
                            r = max(j - i - 1, r)
                        break
                    elif forts[j] != 0:
                        break
            elif forts[i] == -1:
                for j in range(i + 1, len(forts)):
                    if forts[j] == 1:
                        if all(f == 0 for f in forts[i + 1: j]):
                            r = max(j - i - 1, r)
                        break
                    elif forts[j] != 0:
                        break

            i += 1

        return r

                
        
solution_instance = Solution()
print(solution_instance.captureForts([1,0,0,-1,0,0,0,0,1]))  
print(solution_instance.captureForts([0,0,1,-1]))