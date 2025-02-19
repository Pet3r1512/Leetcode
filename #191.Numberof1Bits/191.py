class Solution:
    def hammingWeight(self, n: int) -> int:
        binary = bin(n)[2:]

        result = 0
        for c in binary:
            if c == "1":
                result += 1
        
        return result

solution_instance = Solution()
print(solution_instance.hammingWeight(11))