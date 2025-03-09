class Solution:
    def getLucky(self, s: str, k: int) -> int:
        al = {chr(i): i - 96 for i in range(97, 123)}

        s1 = ""

        for c in s:
            s1 += str(al[c])

        i = 1
        result = []

        while i <= k:
            r = 0
            for c in s1:
                r += int(c)

            result.append(r)
            s1 = str(result[i - 1])
            i += 1

        return result[-1]

solution_instance = Solution()
print(solution_instance.getLucky("leetcode", 2))  