from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        h, w = len(grid), len(grid[0])

        for _ in range(k):
            # create a 0 matrix with the same size of grid
            result = [[0] * w for _ in range(h)]

            for i in range(h):
                for j in range(w):
                    # default move: shift right
                    new_i, new_j = i, j + 1

                    # if the end of a row -> move down to next row
                    if new_j == w:
                        new_i, new_j = i + 1, 0

                    # if the end of a matrix -> go to (0,0)
                    if new_i == h:
                        new_i = 0

                    # start to shift elements
                    result[new_i][new_j] = grid[i][j]

            # update grid after each shift
            grid = result

        return grid


solution_instance = Solution()

print(solution_instance.shiftGrid([[1,2,3],[4,5,6],[7,8,9]], 1))
print(solution_instance.shiftGrid([[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], 4))