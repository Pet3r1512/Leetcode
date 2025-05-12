class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        
        diff = 0
        set1, set2 = set(), set()
        for i in range(len(s1)):
            set1.add(s1[i])
            set2.add(s2[i])
            if s1[i] != s2[i]:
                diff += 1
                if diff > 2:
                    return False
        
        if len(set1) != len(set2) or sorted(set1) != sorted(set2):
            return False
        
        return True



solution_instance = Solution()
print(solution_instance.areAlmostEqual("bank", "kanb"))  
print(solution_instance.areAlmostEqual("attack", "defend"))
print(solution_instance.areAlmostEqual("kelb", "kelb"))