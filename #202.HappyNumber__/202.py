class Solution:
    def isHappy(self, n: int) -> bool:
        # 1 and 7 are happy numbers
        if n == 1 or n == 7:
            return True
        
        result = n
        while result != 1:
            # when result has 1 digit, if it is not 1 and 7 => not happy number => break
            if result < 10 and result != 1 and result != 7:
                result = 0
                break
            s = 0
            # loop for calculate sum of square of all digits
            while result > 0:
                last = result % 10
                s += pow(last, 2)
                result //= 10
            # if s return to n => infinite loop => not happy number
            if s == n:
                break
            # continute to calculate the new number
            result = s

        # if result is 1 => happy number
        if result == 1:
            return True
        # otherwise, it is not happy number
        return False


solution_instance = Solution()
print(solution_instance.isHappy(188))
print(solution_instance.isHappy(2))
print(solution_instance.isHappy(19))