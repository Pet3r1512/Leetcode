from typing import List


class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        size = len(grid) - 2

        blank_matrix = [([0] * size) for i in range(size)]

        for i in range(len(blank_matrix)):
            for j in range(len(blank_matrix[i])):
                cx, cy = i + 1, j + 1

                ar = [
                    grid[cx][cy],
                    grid[cx + 1][cy],
                    grid[cx + 1][cy + 1],
                    grid[cx][cy + 1],
                    grid[cx - 1][cy + 1],
                    grid[cx - 1][cy],
                    grid[cx - 1][cy - 1],
                    grid[cx][cy - 1],
                    grid[cx + 1][cy - 1]
                ]

                blank_matrix[i][j] = max(ar)

        return blank_matrix

solution_instance = Solution()
print(solution_instance.largestLocal([[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]])) 
print(solution_instance.largestLocal([[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]]))