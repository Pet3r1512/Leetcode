class Solution:
    def mySqrt(self, x: int) -> int:
        if x > 2**31 - 1 or x < 0:
            return
        elif x == 0:
            return 0
        else:
            left = 1
            right = x
            while (left <= right):
                mid = left + (right - left)//2
                if(mid == x//mid):
                    return mid
                elif (mid > x//mid):
                    right = mid - 1
                else:
                    left = mid + 1
            return right

solution_instance = Solution()
print(solution_instance.mySqrt(8))