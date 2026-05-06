class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # this problem asks us to return an array of integers
        # where the integers are the products of every integer
        # in the array not including itself
        # I would solve this problem by traversing the array 
        # all the way through one time multiplying all the integers
        # and then traverse it again and divide the total integer
        # multiplication by the integer i am currently on and store
        # it in the array
        #
        # if i were to solve it without division i would do two passes
        # of multiplication.
        # in the first pass I would create an array and store the result of
        # multiplying the number one index before the one i am on with the
        # result of that same number that is one index before since it will
        # already be calculated.
        #   -this would require that the initial array position be 1 since 
        #    we cant multiply the number in the zeroth index of the nums arr
        #    with anything "before" it since its the first.
        # once the multiplication of each number before the current one I am on
        # is done, we can start the second pass
        # the second pass will traverse the nums array backwards and multiply
        # each result stored with the numbers that come after its corresponding
        # number. after the multiplication is done, the postfix number will be
        # multiplied by the factor/number i am on to multiply the following
        # result by the correct number
        #   - the initial case for the post fix number would be 1 because
        #     in the first pass the last number in the nums array is never 
        #     multiplied. therefore it is already the correct number and does
        #     not need any adjustment

        res = [1] * len(nums)
        for i in range(1, len(nums)):
            res[i] = res[i-1] * nums[i-1]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
