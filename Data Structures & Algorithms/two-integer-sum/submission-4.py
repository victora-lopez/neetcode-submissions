class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # this question asks us to return the indices of 
        # two integers in an array given to us that add up
        # to some target value
        #
        # can solve this by calculating the complement of
        # the values in the array and checking if we have
        # come across that complement value at some point
        # in the array. If not we store the value we are 
        # currently on in a hashmap along with it's index
        # we keep going through the array until we find the
        # pair since it is guaranteed
        #
        # input: array of integers and a target integer
        # output: indexes of the two values that add up
        # to the target  value
        #
        # since it asks us to return the smaller index first,
        # we can return it as an array where the first index of
        # that array uses the min() function and the second uses
        # the max() function to return the indices in the proper order

        numMap = {}
        for i in range(len(nums)):
            num = nums[i]
            complement = target - num
            if complement in numMap.keys():
                compIndex = numMap[complement]
                return [min(i, compIndex), max(i, compIndex)]
            numMap[num] = i