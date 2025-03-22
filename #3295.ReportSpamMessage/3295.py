from typing import List


class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        keys = set(bannedWords)
        count = 0
        for word in message:
            if word in keys:
                count += 1
            if count >= 2:
                return True
        return False

solution_instance = Solution()
print(solution_instance.reportSpam(["s","a","aj","ps","h","ou","e","i","x"], ["j","a","b","fa","z","a","no","ih","nq"]))