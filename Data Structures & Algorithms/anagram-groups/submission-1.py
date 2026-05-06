class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # can use a hashmap and use the sorted strings as keys to the map
        # if a new key is made then we create a new entry in the map and 
        # let it's value be an empty array
        # after the new entry is made we can append the string to the hashmap
        # if the the key is one we have already come across, we just append
        # the string to it's corresponding array
        anagramMap = {}
        for i in range(len(strs)):
            key = "".join(sorted(strs[i]))
            if key not in anagramMap.keys():
                anagramMap[key] = []
            anagramMap[key].append(strs[i])
        return anagramMap.values()
