from typing import List


class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        played = [False] * n
        i = 0
        step = 1

        while not played[i]:
            played[i] = True
            i = (i + step * k) % n
            step += 1

        return [j + 1 for j in range(n) if not played[j]]

solution_instance = Solution()
print(solution_instance.circularGameLosers(5, 4))  
print(solution_instance.circularGameLosers(4, 4))