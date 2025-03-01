class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        
        if n == 1:
            return True
        
        if n % 3 == 0:
            return self.isPowerOfThree(n // 3)
        
        return False

    
solution_instance = Solution()
print(solution_instance.isPowerOfThree(45))  
print(solution_instance.isPowerOfThree(27))  