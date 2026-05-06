class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # the question asks to return true or false
        # based on whether true strings are anagrams
        # of each other
        # 
        # we can solve this by looping through each string
        # individually and store them in their respective 
        # hashmaps which will hold the characters as the key
        # and the value will be the count of that character in
        # the string
        # we then compare the hashmaps to see if they are equal
        # and return true or false based on that
        # we can immediately return false if the strings are of different
        # lengths
        # inputs: 2 strings
        # output: bool

        if len(s) != len(t):
            return False

        tMap,sMap = {},{}

        for i in range(len(s)):
            sMap[s[i]] = sMap.get(s[i], 0) + 1
            tMap[t[i]] = tMap.get(t[i], 0) + 1
        
        return tMap == sMap