class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "").lower()

        if len(s) < 1:
            return True

        cleaned_s = ''.join(char for char in s if char.isalnum())

        for i in range(len(cleaned_s)//2):
            if cleaned_s[i] != cleaned_s[len(cleaned_s) - i - 1]:
                return False
            
        return True




solution_instance = Solution()
print(solution_instance.isPalindrome("A man, a plan, a canal: Panama"))
print(solution_instance.isPalindrome("race a car"))