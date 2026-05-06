class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # can find the pair since if they add up they meet the target
        # therefore we can store numbers that we have come across in a hashmap
        # and store the index with it
        # we can calculate the number we are looking for to meet the target and
        # check the hashmap to see if we have come across it yet
        # if it has been stored then we can return the current index we are at
        # and return the index we stored as well
        numMap = {}
        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in numMap:
                return [numMap[compliment], i]
            numMap[nums[i]] = i