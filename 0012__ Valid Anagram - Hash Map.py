class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        s_map={}
        t_map ={}
    
        for i in range(0, len(s)):
            s_ch=s[i]
            t_ch = t[i]
            s_map[s_ch]=s_map.get(s_ch,0)+1
            t_map[t_ch]=t_map.get(t_ch,0)+1
        
        return s_map == t_map
        
s1='anagram'
s2 ='nagaram'
s = Solution()
print(s.isAnagram(s1,s2))