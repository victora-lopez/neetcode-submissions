class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # we can use two pointers to add and remove
        # characters to a set and also keep track on
        # how big our window is of the substring
        # we can add chararacters to the set of characters
        # and we can also check if the character is already in the 
        # character set. if it is we can move the left pointer
        # up and remove every character until the first occurence
        # of the repeated character is removed
        # we can also calculate the length of the substring in 
        # each iteration and check if the length is the longest
        # one
        # if it is the we reassign the longest value
        # if not then just leave the longest value alone.

        l = 0
        longest = 0
        charSet = set()

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            length = r - l + 1 # have to add one because python is 0 indexed
            longest = max(length, longest)
        return longest