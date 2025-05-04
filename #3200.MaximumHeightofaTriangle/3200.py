class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        height = 0
        total = 0

        while total + height + 1 <= red + blue:
            height += 1
            total += height

        def triangle(red_first: bool, red: int, blue: int) -> int :
            line = 0

            for i in range(1, height + 1):
                if (i % 2 == 1 and red_first) or (i % 2 == 0 and not red_first):
                    if red >= i:
                        red -= i
                        line += 1
                    else:
                        break
                else:
                    if blue >= i:
                        blue -= i
                        line += 1
                    else:
                        break
            return line
        
        return max(triangle(True, red, blue), triangle(False, red, blue))

solution_instance = Solution()
print(solution_instance.maxHeightOfTriangle(2, 4))  
print(solution_instance.maxHeightOfTriangle(2, 1))
print(solution_instance.maxHeightOfTriangle(10, 1))