class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # use to bucket sort arrays of sizee 26 (1 index for each letter of the alphabet)
        # each index will hold the count of each letter in the strings
        # we will compare these two arrays at each index and if their counts match then we will
        # increment a match counter by 1.
        # if we lose a match by going over or below the count for our comparator string s1 then
        # we decrement it by 1
        
        if len(s1) > len(s2):
            return False

        s1Count, s2Count = [0] * 26, [0] * 26
        match = 0

        for i in range(len(s1)):
            s1index = ord(s1[i]) - ord('a')
            s2index = ord(s2[i]) - ord('a')
            s1Count[s1index] += 1
            s2Count[s2index] += 1
        
        for i in range(26):
            if s1Count[i] == s2Count[i]:
                match += 1

        l = 0
        for r in range(len(s1), len(s2)):
            if match == 26:
                return True
            
            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1

            if s1Count[index] == s2Count[index]:
                match += 1
            elif s1Count[index] + 1 == s2Count[index]: # this tells us we went over the limit and serves as a barrier to not keep -= 1 each time it doesnt match
                match -= 1
            
            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1

            if s1Count[index] == s2Count[index]:
                match += 1
            elif s1Count[index] - 1 == s2Count[index]: # this tells us we went over the limit and serves as a barrier to not keep -= 1 each time it doesnt match
                match -= 1
            
            l += 1
        
        if match == 26:
            return True
        
        return False