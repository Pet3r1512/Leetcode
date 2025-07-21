class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        # reverser string
        # return str(int(num[::-1]))[::-1]

        # while loop

        last_index = len(num) - 1

        while last_index > 0:
            if num[last_index] != "0":
                break
            last_index -= 1

        return num[: last_index + 1]

solution_instance = Solution()
print(solution_instance.removeTrailingZeros("51230100")) 
print(solution_instance.removeTrailingZeros("123"))