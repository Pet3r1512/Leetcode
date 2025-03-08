from typing import List

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        r1 = "qwertyuiop"
        r2 = "asdfghjkl"
        r3 = "zxcvbnm"

        result = []

        for word in words:
            s = set()
            for letter in word:
                lower = letter.lower()
                if lower in r1:
                    s.add(1)
                elif lower in r2:
                    s.add(2)
                else:
                    s.add(3)    
                
                if len(s) > 1:
                    break

            if len(s) == 1:
                result.append(word)

        return result

solution_instance = Solution()
print(solution_instance.findWords(["Hello","Alaska","Dad","Peace"]))  