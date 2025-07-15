class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        r = ""

        for c in word:
            if c.isalpha():
                r += "_"
            else:
                r += c

        return len(set([int(e) for e in r.split("_") if e.isdigit()]))


solution_instance = Solution()
print(solution_instance.numDifferentIntegers("a123bc34d8ef34")) 
print(solution_instance.numDifferentIntegers("leet1234code234"))
print(solution_instance.numDifferentIntegers("a1b01c001"))