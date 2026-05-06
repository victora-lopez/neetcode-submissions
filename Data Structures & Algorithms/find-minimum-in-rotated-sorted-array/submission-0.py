class Solution:
    def findMin(self, nums: List[int]) -> int:
        # one way to find the minimum would be running 
        # a binary search normally and checking which direction has
        # a smaller number when halving going to the next half
        # we can maybe use our low and high pointer to determine which direction to go in?
        # if our high pointer contains the smaller number then the minimum would be before it
        # if the low pointer has the smaller number then we can go in that direction to check
        # if the minimum was there
        # can only get smaller from high pointer and can only get bigger from low pointer
        # maybe move pointers based on which one is bigger?
        # keep the smaller pointer in place and adjust the one with a larger number?
        #   i.e if the number in the middle is larger than the larger pointer, move the 
        #    larger pointer, if we move smaller one we might miss the minimum.
        #   if the middle is smaller than the smallest pointer then we can move the smaller
        #   pointer to it.
        #       continue to do this until the pointers meet?
        #   if the number falls between the two,
        #
        # question basicallly wants us to move towards the minimum number.
        #   -therefore if the middle number is bigger than the number at the end
        #    we move the start pointer up to the middle + 1. (dont have to check mid again)
        #   -if it is smaller, then we know the start pointer is in the direction of the
        #    min so we move the end pointer to the middle - 1.
        #
        # input: an array of ints rotated n times
        # output: integer that is the minimum of the input array
        #
        # steps:
        # 1. initialize left and right pointer to first and last index of the array
        # 2. set conditions on the loop to iterate until the left and right pointer meet
        # 3. in the loop test to see if the middle is larger than the value at the end index
        #    if it is then move the start pointer up
        #    else move the end pointer down
        # 4. keep looping until the start and end pointer meet.
        # 5. return the minimum between the the current known min value and the value where
        #    the start pointer met the end pointer.

        start, end = 0, len(nums) - 1
        minNum = nums[0]

        while start < end:
            mid = start + (end-start) // 2
            minNum = min(minNum, nums[mid])
            if nums[mid] > nums[end]:
                start = mid + 1
            else:
                end = mid - 1
        minNum = min(minNum, nums[start])
        return minNum
