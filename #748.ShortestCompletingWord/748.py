from typing import List
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        l = licensePlate.lower().replace(" ", "")
        d = dict()
        r = []
        for letter in l:
            if letter.isalpha():
                if letter not in d:
                    d[letter] = 1
                else:
                    d[letter] += 1
        for word in words:
            clone = d.copy()
            for letter in word:
                if letter in clone:
                    clone[letter] -= 1
                    if clone[letter] <= 0:
                        clone.pop(letter)
            if len(clone) == 0:
                r.append(word)
        if not r:
            return ""
        result = r[0]
        for word in r:
            if len(word) < len(result):
                result = word
        return result

solution_instance = Solution()
print(solution_instance.shortestCompletingWord("Ah71752", ["suggest","letter","of","husband","easy","education","drug","prevent","writer","old"])) 
print(solution_instance.shortestCompletingWord("1s3 456", ["looks","pest","stew","show"])) 
print(solution_instance.shortestCompletingWord("1s3 PSt", ["step","steps","stripe","stepple"])) 
print(solution_instance.shortestCompletingWord("TE73696", ["ten","two","better","talk","suddenly","stand","protect","collection","about","southern"])) 
print(solution_instance.shortestCompletingWord("AN87005", ["participant","individual","start","exist","above","already","easy","attack","player","important"])) 