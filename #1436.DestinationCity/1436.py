from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        start = []

        for path in paths:
            start.append(path[0])

        for path in paths:
            if path[1] not in start:
                return path[1]
        return paths[0][1]

solution_instance = Solution()
print(solution_instance.destCity([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]))  
print(solution_instance.destCity([["B","C"],["D","B"],["C","A"]]))  