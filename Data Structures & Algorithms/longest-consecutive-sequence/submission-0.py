class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # problem asks us to returns the length of 
        # the longest consecutive sequence
        # input: list of nums
        # output: integer of length LCS
        #
        # can use a variable to store the length of the longest
        # sequence
        # we can store the nums array as a set and check
        # if num+1 is in the set if it is set num to num + 1
        # and check if num + 1 is in the set repeatedly
        # once we hit the end of that sequence we store how long
        # it was.
        # we also need to check if each number is the start of a 
        # sequence by seeing if the number before it is in the set
        # if it is, then it is already part of a sequence and we don't
        # need to check it's length
        # if nums-1 doesn't exist, then we know it is the start of a sequence
        # this basically allows us to only check unique sequences
        # rather than each individual number in the set
        # making it where each number is only processed once.

        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest
