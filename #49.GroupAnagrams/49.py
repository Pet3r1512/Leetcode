from typing import List
from collections import Counter, defaultdict

# Idea-----------
# Create a dictionary for all char in a string
# Combine all strings with them same dictionary into a dictionary where key is dictionary in step 1 and values are all string with exactly same dictionary
# return dictionary's values


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grps = defaultdict(list)

        for s in strs:
            keys = tuple(sorted(Counter(s).items()))
            grps[keys].append(s)

        return list(grps.values())

solution_instance = Solution()
print(solution_instance.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))  
print(solution_instance.groupAnagrams([""]))
print(solution_instance.groupAnagrams(["a"]))