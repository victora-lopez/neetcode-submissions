class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Question asks us to find the container that will hold the most
        # water and return how much water the container can hold
        #
        # input: array of heights as ints
        # output: int of how much water biggest container holds
        # 
        # it seems like you optimally want the tallest possible containers
        # that are as far away from each other as possible
        # ideally there tallest heights are at the beginning and end of the
        # array, but will commonly not be the case
        # we use two pointers at the start and end of the array
        # and calculate the area using the smaller height of the two
        # and see how much water the container holds
        # we can then compare it to a variable that holds the max water
        # container so far and if the container we are on holds more water 
        # we can update that variable value and continue scanning to see
        # if there is another container that holds more water
        # once the left pointer and right pointer meet we can return the max
        # water variable. I forgot but we also need to update the pointers.
        # we can move the pointer with the smaller height up or down one 
        # depending if it is left or right.
        #
        # plan:
        # 1: initialize two pointers
        # 2: loop through array with the pointers
        # 3: calculate the area of water using the smaller height of the two and the distance between them
        # 4: check if area is larger than largest one recorded and update pointers
        # 5: repeat steps 2-4 until left and right pointer meet
        # 6: return max water variable
        
        l,r = 0, len(heights) - 1
        maxWater = 0

        while l < r:
            smallerHeight = min(heights[l], heights[r])
            distance = r - l
            waterArea = smallerHeight * distance
            maxWater = max(waterArea, maxWater)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return maxWater






