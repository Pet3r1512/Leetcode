from typing import List


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []

        for log in logs:
            s = log.split("/")
            if s[0] == "..":
                if stack:
                    stack.pop()
            elif s[0] == ".":
                continue
            else:
                stack.append(s[0])

        return len(stack)

solution_instance = Solution()
print(solution_instance.minOperations(["d1/","d2/","./","d3/","../","d31/"]))
print(solution_instance.minOperations(["d1/","../","../","../"])) 
print(solution_instance.minOperations(["d1/","d2/","../","d21/","./"])) 