class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictionaryS = {}
        dictionaryT = {}
        for letter in s:
            if letter not in dictionaryS.keys():
                dictionaryS[letter] = 1
            else:
                dictionaryS[letter] += 1
        for letter in t:
            if letter not in dictionaryT.keys():
                dictionaryT[letter] = 1
            else:
                dictionaryT[letter] += 1
        return dictionaryS ==  dictionaryT