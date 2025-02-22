class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n >0 and str(bin(n)).count("1") == 1

solution_instance = Solution()
print(solution_instance.isPowerOfTwo(1048)) 
print(solution_instance.isPowerOfTwo(1024)) 
print(solution_instance.isPowerOfTwo(32)) 