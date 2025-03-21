from typing import List

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        r = []
        for i in range(len(words)):
            if x in words[i]:
                r.append(i)

        return r


solution_instance = Solution()
print(solution_instance.findWordsContaining(["leet","code"], "e")) 