class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False

        elif n == 1:
            return True
        
        else:
            for i in [2, 3, 5]:
                while n % i == 0:
                    n = n // i

        return n == 1

solution_instance = Solution()
print(solution_instance.isUgly(6))  
print(solution_instance.isUgly(14))  