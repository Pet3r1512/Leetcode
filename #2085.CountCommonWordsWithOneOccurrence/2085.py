from collections import Counter
from typing import List

class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        # My Way
        # s = set(words1 + words2)
        # c = 0

        # for w in s:
        #     if words1.count(w) == 1 and words2.count(w) == 1:
        #         c += 1

        # return c

        # Improved
        c1 = Counter(words1)
        c2 = Counter(words2)

        return sum(1 for w in c1 if c1[w] == 1 and c2[w] == 1)

solution_instance = Solution()
print(solution_instance.countWords(["leetcode","is","amazing","as","is"], ["amazing","leetcode","is"]))  
print(solution_instance.countWords(["a","ab"], ["a","a","a","ab"]))  