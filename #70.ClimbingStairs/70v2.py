class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 1 or n >= 45:
            return
        
        if n == 1:
            return 1
        
        if n == 2:
            return 2
        
        init_steps = [1, 1] # the last 2 steps are always 1
        n -= 2 # skip 2 last elements
        cursor = len(init_steps) - 1

        while n >= 0:
            next_steps = init_steps[cursor] + init_steps[cursor - 1]
            init_steps.insert(0, next_steps)
            n -= 1

        return init_steps[0]
            

solution_instance = Solution()
print(solution_instance.climbStairs(5))