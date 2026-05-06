class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complimentMap = {}
        for i,num in enumerate(nums):
            compliment = target - num
            if num in complimentMap:
                return [complimentMap[num], i]
            complimentMap[compliment] = i