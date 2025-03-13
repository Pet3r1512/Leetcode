class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # my Solution
        # ss = ''.join(sorted(s))
        # st = ''.join(sorted(t))

        # for i in range(len(ss)):
        #     if ss[i] != st[i]:
        #         return st[i]

        # return st[-1]


        # leanred version
        for c in t:
            if s.count(c) != t.count(c):
                return c

solution_instance = Solution()
print(solution_instance.findTheDifference("abcd", "abcde"))
