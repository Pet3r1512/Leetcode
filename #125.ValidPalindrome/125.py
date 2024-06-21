import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        if(len(s) <= 1):
            return True
        s = re.sub(r'[^A-Za-z0-9]', '', s).lower()
        testStr = s[::-1]
        return s == testStr

solution_instance = Solution()
print(solution_instance.isPalindrome("race a car"))