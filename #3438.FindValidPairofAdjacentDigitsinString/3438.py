class Solution:
    def findValidPair(self, s: str) -> str:
        d = dict()

        for c in s:
            d[c] = 1 + d.get(c, 0)

        for i in range(len(s) - 1):
            if s[i] != s[i + 1] and int(d[s[i]]) == int(s[i]) and int(d[s[i + 1]]) == int(s[i + 1]):
                return str(s[i]) + str(s[i + 1])
            
        return ""


solution_instance = Solution()
print(solution_instance.findValidPair("2523533"))  
print(solution_instance.findValidPair("221"))
print(solution_instance.findValidPair("22"))