from typing import List


class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        def convert_to_minute(time: str) -> str:
            hour = time.split(":")[0]
            minute = time.split(":")[1]
            return hour * 60 + minute
        
        s1, e1 = map(convert_to_minute, event1)
        s2, e2 = map(convert_to_minute, event2)

        return not (e1 < s2 or e2 < s1)


solution_instance = Solution()
print(solution_instance.haveConflict(["01:15","02:00"], ["02:00","03:00"]))
print(solution_instance.haveConflict(["01:00","02:00"], ["01:20","03:00"])) 
print(solution_instance.haveConflict(["10:00","11:00"], ["14:00","15:00"])) 