class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # this question asks us to return a list that groups all the
        # different type of anagrams
        # input: array of strings
        # output: an array that contains arrays of strings
        # separated by if they are anagrams of each other
        #
        # we can solve this by using an array that holds the count of each
        # character and the index corresponds to the character
        # i.e. a is index 0, b index 1, c index 2, ..., z index 25
        # we use this as the key for a hashmap, where the value associated
        # with the key is an array that holds the string we counted the
        # characters of.
        #
        # To make the key usable we have to type case the array as a tuple
        # so it is immutable, and this works because if two strings use the
        # exact same characters, their count arrays will be the same:
        # example:
        # 'cat': [1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0]
        # 'act': [1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0]
        # once casted it can be used as a key since lists arent allowed to
        # in python.
        # if it is a new key we can set the value as an empty array
        # then append the string to that array
        # if it isn't then we just append the array directly
        #
        # to wrap up the problem we can return the values of the
        # dictionary/hashmap

        ans = {}
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c)-ord('a')] += 1
            if tuple(count) not in ans.keys():
                ans[tuple(count)] = []
            ans[tuple(count)].append(s)
        return ans.values()
            
