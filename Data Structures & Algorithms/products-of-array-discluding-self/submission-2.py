class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # to find the product of every num in the array except itself
        # we have to multiply all of the factors before the current number
        # and all of the numbers that come after that number
        # we can do this by traversing the array one time forwards which
        # multiplies the numbers before the current one and store it in 
        # it's place
        # the second traversal will be in reverse and multiply each number
        # by a postfix, which is the factors that come after the number
        # multiplied together
        #  [1 2 4 6] --> [1 1 1 1] --> [1 1 2 8] --> [48  24  12  8]

        prod = [1] * len(nums)

        for i in range(1, len(nums)):
            prod[i] = nums[i - 1] * prod[i - 1]
        
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            prod[i] *= postfix
            postfix *= nums[i]
        return prod