class Solution:
    # want to encode the list of strings to be a singluar string concatenating
    # all the strings with the following pattern:
    # len(str1)#strlen(str2)#str2...
    # ex: 3#cat6#lovely
    def encode(self, strs: List[str]) -> str:
        ans = ""
        for s in strs:
            s_len = str(len(s))
            ans += s_len + '#' + s
        return ans

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            str_len = int(s[i:j])
            i = j + 1
            j = i + str_len
            encoded_str = s[i:j]
            ans.append(encoded_str)
            i = j
        return ans
