class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        dict_s_t = dict()
        dict_t_s = dict()

        for cs, ct in zip(s, t):
            if (cs in dict_s_t and dict_s_t[cs] != ct) or (ct in dict_t_s and dict_t_s[ct] != cs):
                return False
        
            dict_s_t[cs] = ct
            dict_t_s[ct] = cs

        return True



solution_instance = Solution()
print(solution_instance.isIsomorphic("badc", "baba"))  