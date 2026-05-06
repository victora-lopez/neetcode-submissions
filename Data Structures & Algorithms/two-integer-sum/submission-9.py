class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complimentMap = {}
        for i in range(len(nums)):
            compliment = target - nums[i]
            if nums[i] in complimentMap.keys():
                return [complimentMap[nums[i]], i]
            complimentMap[compliment] = i