class Solution:
    def countEven(self, num: int) -> int:
        r = 0

        for i in range(1, num + 1):
            if sum(list(map(int, str(i)))) % 2 == 0:
                r += 1

        return r
        

solution_instance = Solution()
print(solution_instance.countEven(4))  
print(solution_instance.countEven(30))