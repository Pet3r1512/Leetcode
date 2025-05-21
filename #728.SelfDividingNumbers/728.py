from typing import List


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        r = []

        for i in range(left, right + 1):
            if i < 10:
                r.append(i)
            elif "0" in str(i):
                continue
            else:
                is_valid = True
                for digit in str(i):
                    if i % int(digit) != 0:
                        is_valid = False
                        break
                if is_valid == True:
                    r.append(i)
        return r

solution_instance = Solution()
print(solution_instance.selfDividingNumbers(1, 22))  
print(solution_instance.selfDividingNumbers(47, 85))