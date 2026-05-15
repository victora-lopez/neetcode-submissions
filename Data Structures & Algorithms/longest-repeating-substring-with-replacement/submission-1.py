class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq: dict = {}
        l: int = 0
        maxFreq: int = 0
        longest: int = 0

        for r in range(len(s)):
            freq[s[r]] = 1 + freq.get(s[r], 0)
            maxFreq = max(maxFreq, freq[s[r]])

            while (r - l + 1) - maxFreq > k:
                freq[s[l]] -= 1
                l += 1
            
            longest = max(longest, r - l + 1)

        return longest