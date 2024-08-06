class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if (len(a) > 10**4 or len(b) > 10**4):
            return
        setA = set(a)
        setB = set(b)
        validSet = {"0", "1"}

        if(validSet == setA or setA == {"0"} or setA == {"1"}) and (validSet == setB or setB == {"0"} or setB == {"1"}):
            return str(bin(int(a, 2) + int(b, 2)))[2:]
        
solution_instance = Solution()
print(solution_instance.addBinary("11", "1"))
