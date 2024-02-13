from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if (len(strs) == 0):
            return ""
        # if input List of string is empty then return "" because there will be no string at all
        for i in range(len(strs[0])): #For each letter in the first word
            c = strs[0][i]              # take the letter at position i and assign it for c
            for j in range(1, len(strs)):   # compare the letter at position i with remain strings in the List
                if (i == len(strs[j]) or strs[j][i] != c): # if i is longer than the word at j or the letter at position i in the j's tring is different 
                    return strs[0][:i]        #then return the string from 0 to i-1
        return strs[0]
        


solution_instance = Solution()

print(solution_instance.longestCommonPrefix(["flower","flow","flight"]))