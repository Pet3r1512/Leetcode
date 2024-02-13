class Solution:
    def isPalindrome(self, x: int) -> bool:
        def reverseNumber(x: int):
            result = 0
            while x != 0:
                digit = x % 10
                result = result * 10 + digit
                x //= 10
            return result
        
        if(x >= 0):
            if(x == reverseNumber(x)):
                return True
        else:
            x = abs(x)
            if(x == reverseNumber(x)):
                newX = reverseNumber(x)
                if (str(x) == str(newX) + "-"):
                    return True
        return False

solution_instance = Solution()

print(solution_instance.isPalindrome(-121))