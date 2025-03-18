from typing import List


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        # Solution 1
        s1 = ""
        s2 = ""

        for word in word1:
            s1 += word

        for word in word2:
            s2 += word
        
        return s1 == s2

        # Solution 2
        # return "".join(word1) == "".join(word2)

solution_instance = Solution()
print(solution_instance.arrayStringsAreEqual(["ab", "c"],["a", "bc"]))  