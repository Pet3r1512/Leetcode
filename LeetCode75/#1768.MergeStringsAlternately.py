class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p1, p2 = 0, 0
        r = ""

        while p1 < len(word1) and p2 < len(word2):
            r += word1[p1] + word2[p2]
            p1 += 1
            p2 += 1
        
        return r + word1[p1:] + word2[p2:]


solution_instance = Solution()
print(solution_instance.mergeAlternately("abc", "pqr"))
print(solution_instance.mergeAlternately("ab", "pqrs"))
print(solution_instance.mergeAlternately("abcd", "pq"))