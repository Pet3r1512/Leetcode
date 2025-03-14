from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        r = [""] * len(score)
        
        i = 0

        while i < len(score):
            mx = max(score)
            idx = score.index(mx)
            print(str(mx) + " at " + str(idx) + " " + str(i))
            if score[idx] == 0:
                r[idx] = str(len(score) - 1)
            match i:
                case 0:
                    r[idx] = "Gold Medal"
                case 1:
                    r[idx] = "Silver Medal"
                case 2: 
                    r[idx] = "Bronze Medal"
                case _:
                    r[idx] = str(i + 1)
                
            print(r)
            score[idx] = -1
            i += 1
        return r

                       
solution_instance = Solution()
print(solution_instance.findRelativeRanks([123123,11921,1,0,123])) 