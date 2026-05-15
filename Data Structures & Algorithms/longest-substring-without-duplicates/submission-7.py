class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charMap: dict = {}
        l, r = 0,0
        longest = 0

        for r in range(len(s)):
            if s[r] in charMap:
                l = max(charMap[s[r]] + 1, l)
            charMap[s[r]] = r
            longest = max(longest, r - l + 1)
        return longest