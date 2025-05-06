from typing import List


class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        # idea:
        # Step 1: Rotate the matrix 90 degree clockwise
        # Step 2: Calculate and replace values
        # Step 3: Rotate the matrix 90 degree anti-clockwise

        rows = len(matrix)
        cols = len(matrix[0]) if rows > 0 else 0

        rotated = [[0] * rows for _ in range(cols)]

        for i in range(rows):
            for j in range(cols):
                rotated[j][rows - i - 1] = matrix[i][j]

        for i in range(len(rotated)):
            max_value = max([val for val in rotated[i] if val != -1], default=0)
            for j in range(len(rotated[i])):
                if rotated[i][j] == -1:
                    rotated[i][j] = max_value

        restored = [[0] * cols for _ in range(rows)]

        for i in range(cols):
            for j in range(rows):
                restored[rows - j - 1][i] = rotated[i][j]

        return restored


solution_instance = Solution()
print(solution_instance.modifiedMatrix([[1,2,-1],[4,-1,6],[7,8,9]]))  
print(solution_instance.modifiedMatrix([[3,-1],[5,2]]))