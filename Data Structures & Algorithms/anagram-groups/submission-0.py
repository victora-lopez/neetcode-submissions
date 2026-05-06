class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # can use a hashmap to group together the anagrams
        # since an anagram uses the same letters the same number of times,
        # we can sort the strings and use that as the key for our hash map
        # the value for our hash map will be the array the will hold the anagrams
        # at the end we can return the values of our hash map
        anagram = {}

        for s in strs:
            key = "".join(sorted(s))
            if key not in anagram:
                anagram[key] = []
            anagram[key].append(s)
        return anagram.values()
        