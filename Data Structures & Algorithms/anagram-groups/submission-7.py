class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # need to store the list of anagrams with a key that has their characters
        # maybe store the characters as a set and convert to tuple?
        # but need the order of the characters to be the same
        # how to achieve n * m?
        # i can create a bucket that stores the count of each character in an array and
        # then turn that into a tuple for the key
        # with that i can store the anagrams
        #
        # i.e: index 0 refers to a, 1 to b, 2 to c, ..., 25 with z
        # (0, 1, ..., 25) -> key, value: ['act', 'cat']
        # in the end retreive the list of values from each key and append them to a list

        anagramMap = defaultdict(list)
        ans = []
        for s in strs:
            key = [0] * 26
            for c in s:
                key[ord(c)-ord('a')] += 1
            key = tuple(key) #key must be immutable data type
            anagramMap[key].append(s)
        

        return list(anagramMap.values())
