class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False
        
        stack = []

        for symbol in s:
            if symbol in "([{":
                stack.append(symbol)

            elif len(stack) > 0:
                if (symbol == ")" and stack.pop() != "(") or (symbol == "]" and stack.pop() != "[") or (symbol == "}" and stack.pop() != "{"):
                    return False
            
        return len(stack) == 0


solution_instance = Solution()

print(solution_instance.isValid("()"))
print(solution_instance.isValid("(){}[]"))
print(solution_instance.isValid("([)]"))