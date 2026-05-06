class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # this question is asking us to return the most frequent
        # integers in the list
        # since we are dealing with frequency, we can use a hashmap
        # to make the number relate to its count
        # we can also store the number in another array where its index
        # indicates how frequently it appears based on its count
        # the purpose of this is that the higher the count is of 
        # a specfic integer the quicker it is to retreive if we 
        # traverse this array in reverse
        # there is an edge case where two numbers are counted the same number
        # of times, and we can only store one number in the array normally.
        # we will have to nest arrays in the array to be able to append more
        # than one number to it.
        #
        # once we have slotted the numbers into the corresponding buckets
        # we can traverse the array in reverse and append the numbers to a
        # result array and return that array.

        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = count.get(num,0) + 1
        for num,count in count.items():
            freq[count].append(num)
        ans = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans

                    
