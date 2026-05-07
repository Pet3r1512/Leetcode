from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        operations = "+-*/"

        for token in tokens:
            if token not in operations:
                s.append(int(token))
            else:
                a = s.pop()
                b = s.pop()

                if token == "+":
                    s.append(b + a)
                elif token == "-":
                    s.append(b - a)
                elif token == "*":
                    s.append(b * a)
                else:
                    if a != 0:
                        s.append(int(b/a))

        return s[0]

solution_instance = Solution()
print(solution_instance.evalRPN((["2","1","+","3","*"])))
print(solution_instance.evalRPN((["4","13","5","/","+"])))
print(solution_instance.evalRPN((["10","6","9","3","+","-11","*","/","*","17","+","5","+"])))