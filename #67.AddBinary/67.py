class Solution:
    def addBinary(self, a: str, b: str) -> str:
        biA = set(a)
        biB = set(b)
        s = {'0', '1'}
        if (s == biA or biA == {'0'} or biA == {'1'}) and (s == biB or biB == {'0'} or biB == {'1'}):
            if(len(a) > 10**4 or len(b) > 10**4):
                return
            return str(bin(int(a,2) + int(b,2)))[2:]
        else :
            return "invalid"
        
solution_instance = Solution()
print(solution_instance.addBinary("11", "1"))
