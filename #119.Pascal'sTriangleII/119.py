from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        arr = [ [0 for _ in range(rowIndex + 1)] for _ in range(rowIndex + 1) ]

        for i in range(rowIndex + 1):
            arr[i][0] = 1
            for j in range(1, i + 1):
                arr[i][j] = arr[i - 1][j - 1] + arr[i - 1][j]

        return [row[: i + 1] for i, row in enumerate(arr)][-1]



solution_instance = Solution()
print(solution_instance.getRow(3))
print(solution_instance.getRow(1))