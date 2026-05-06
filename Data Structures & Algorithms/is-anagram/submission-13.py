class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        sMap = {}
        tMap = {}

        for i in range(len(s)):
            sMap[s[i]] = sMap.get(s[i], 0) + 1
            tMap[t[i]] = tMap.get(t[i], 0) + 1
        
        for c,count in sMap.items():
            if c not in tMap.keys() or tMap[c]!=count:
                return False
        return True
