class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        visit=[]
        if len(s)!=len(t):
            return False
        return sorted(s)==sorted(t)

s1='rat'
s2 ='car'
s = Solution()
print(s.isAnagram(s1,s2))