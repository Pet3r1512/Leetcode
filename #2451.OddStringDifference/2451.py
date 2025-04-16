from typing import List
import string
from collections import Counter

class Solution:
    def oddString(self, words: List[str]) -> str:
        d = {letter: idx for idx, letter in enumerate(string.ascii_lowercase)}
        r = []
        rd = dict()
        for w in words:
            wr = []
            for i in range(len(w) - 1):
                diff = d[w[i + 1]] - d[w[i]]
                wr.append(diff)
            r.append(wr)
            rd[w] = wr
        counter = Counter(tuple(pair) for pair in r)
        unique = []
        for k, v in counter.items():
            if v == 1:
                unique.append(k)
        for k, v in rd.items():
            if v == list(unique[0]):
                return k
solution_instance = Solution()
print(solution_instance.oddString(["adc","wzy","abc"]))  
print(solution_instance.oddString(["aaa","bob","ccc","ddd"]))