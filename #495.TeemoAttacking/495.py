from typing import List

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if duration == 0:
            return 0

        result = 0

        for i in range(len(timeSeries) - 1):
            if timeSeries[i] + duration - 1 < timeSeries[i + 1]:
                result += duration
            else:
                result += timeSeries[i + 1] - timeSeries[i]

        return result + duration


solution_instance = Solution()
print(solution_instance.findPoisonedDuration([1,4], 2)) 
print(solution_instance.findPoisonedDuration([1,2,3,4,5], 5)) 