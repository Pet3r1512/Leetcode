from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                prev_slot = flowerbed[i - 1] if i > 0 else 0
                next_slot = flowerbed[i + 1] if i < len(flowerbed) - 1 else 0

                if prev_slot == 0 and next_slot == 0:
                    flowerbed[i] = 1
                    n -= 1
                    if n == 0:
                        return True
                    
        return n <= 0


solution_instance = Solution()
print(solution_instance.canPlaceFlowers([1,0,0,0,1], 1))  
print(solution_instance.canPlaceFlowers([1,0,0,0,1], 2))