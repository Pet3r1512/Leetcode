class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if(needle not in haystack) or (len(haystack) < len(needle)):
            return -1
        result = 0
        for i in range(len(haystack)):
            if(haystack[i: i + len(needle)] == needle):
                return i
        return -1
        

        
solution_instance = Solution()
print(solution_instance.strStr("hello", "ll"))