class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # We are looking for a duplicate value in the array
        # that is passed to us
        # Input: array of integers 
        # output: boolean true or false based on 
        # if there is a duplicate
        # I think we can loop through the array and store 
        # the integer in a hash map and then move on to the next
        # value.
        #
        # once we move on to the next value, we can check if that value
        # is in the hash map, meaning we have seen it before.
        # if it is then we return true, if not we store it
        # and then go to the next value
        # if we traverse the entire array and don't get a repeated 
        # value then we can return false

        numMap = {}
        for num in nums:
            if num in numMap.keys():
                return True
            else:
                numMap[num] = numMap.get(num, 0) + 1
        return False
        