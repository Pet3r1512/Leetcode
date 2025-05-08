class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        return int(''.join(str(ord(c) - ord('a')) for c in firstWord)) + int(''.join(str(ord(c) - ord('a')) for c in secondWord)) == int(''.join(str(ord(c) - ord('a')) for c in targetWord))

solution_instance = Solution()
print(solution_instance.isSumEqual("acb", "cba", "cdb"))  
print(solution_instance.isSumEqual("aaa", "a", "aab"))