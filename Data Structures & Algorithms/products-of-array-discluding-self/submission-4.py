class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 48 = 1 * 2 * 4 * 6
        # mulp = 1 * 6 * 4 * 2
        # [48 24 12 8]
        #  ^ 
        # [1 2 4 6]
        #    ^

        res = [1] * len(nums)
        product = 1
        
        # forward traversal:
        for i in range(len(nums)):
            product *= nums[i]
            res[i+1] *= product
            if i+2 == len(nums):
                break
        
        product = 1

        # backwards traversal:
        for i in range(len(nums) - 1, 0, -1):
            product *= nums[i]
            res[i-1] *= product
            if i-2 == -1:
                break
        return res