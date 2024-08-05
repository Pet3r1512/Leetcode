from typing import List

class Solution:
    def paint(self, image, sr, sc, color, current):
        if (sr < 0 or sc < 0 or sr >= len(image) or sc >= len(image)):
            return
        if current != image[sr][sc]:
            return
        image[sr][sc] = color
        self.paint(image, sr, sc + 1, color, current)
        self.paint(image, sr + 1, sc, color, current)
        self.paint(image, sr, sc - 1, color, current)
        self.paint(image, sr - 1, sc, color, current)

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        curr = image[sr][sc]

        if(curr == color):
            return image

        if image[sr][sc] == color:
            return image

        self.paint(image, sr, sc, color, image[sr][sc])
        return image


solution_instance = Solution()
print(solution_instance.floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2))