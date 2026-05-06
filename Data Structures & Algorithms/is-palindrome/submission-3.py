class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanStr = "".join(char.lower() for char in s if char.isalnum())
        l,r = 0, len(cleanStr) - 1
        print(cleanStr)

        while l < r:
            if cleanStr[l] != cleanStr[r]:
                return False
            l += 1
            r -= 1
        return True