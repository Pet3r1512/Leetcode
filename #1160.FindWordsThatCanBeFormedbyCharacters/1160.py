from typing import List


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        d = dict()
        r = 0
        for c in chars:
            d[c] = 1 + d.get(c, 0)

        for w in words:
            cpd = d.copy()

            for c in w:
                if c in cpd and cpd[c] > 0:
                    cpd[c] -= 1
                else:
                    break
            else:
                r += len(w)

        return r


solution_instance = Solution()
print(solution_instance.countCharacters(["cat","bt","hat","tree"], "atach"))  
print(solution_instance.countCharacters(["hello","world","leetcode"], "welldonehoneyr"))  
        