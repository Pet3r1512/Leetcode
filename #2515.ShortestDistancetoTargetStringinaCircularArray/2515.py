from typing import List


class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        if target not in words:
            return -1
        
        if (len(words) == 1 and target == words[0]) or (target == words[startIndex]):
            return 0
        
        positions = []

        for i in range(len(words)):
            if words[i] == target:
                positions.append(i)

        result = len(words) - 1
        
        for pos in positions:
            left = right = startIndex
            stepL = stepR = 0
            while left != pos:
                left -= 1
                stepL += 1
                if left < 0:
                    left = len(words) - 1
            if stepL < result:
                result = stepL
            while right != pos:
                right += 1
                stepR += 1
                if right == len(words):
                    right = 0
            if stepR < result:
                result = stepR
        return result


solution_instance = Solution()
print(solution_instance.closestTarget(["hello","i","am","leetcode","hello"], "hello", 1))          
print(solution_instance.closestTarget(["a","b","leetcode"], "leetcode", 0))          
print(solution_instance.closestTarget(["i","eat","leetcode"], "ate",0))          