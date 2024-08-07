class Solution:
    def climbStairs(self, n: int) -> int:
        initSteps = [2, 1, 1]
        n -= 3
        cursor = len(initSteps) - 2
        while(n >= 0):
            nextSteps = initSteps[cursor] + initSteps[cursor - 1]
            initSteps.insert(0, nextSteps)
            n -= 1
            print(initSteps)
        return initSteps[0]
            

solution_instance = Solution()
print(solution_instance.climbStairs(5))