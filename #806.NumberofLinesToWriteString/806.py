import string
from typing import List


class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        d = dict(zip(string.ascii_lowercase, widths))
        ss = 0
        r = [1, 0]

        for c in s:
            if ss + d[c] > 100:
                r[0] += 1
                ss = d[c]
            else:
                ss += d[c]

        r[1] = ss
        return r


solution_instance = Solution()
print(solution_instance.numberOfLines([10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], "abcdefghijklmnopqrstuvwxyz"))  
print(solution_instance.numberOfLines([4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], "bbbcccdddaaa"))