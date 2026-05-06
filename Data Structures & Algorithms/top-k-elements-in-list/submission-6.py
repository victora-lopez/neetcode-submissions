class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # what to sort them in a list where the index - 1 represents the frequency of that value
        # i.e frequency of 1 is stored in index 0, frequency of 3 is stored in index 2, etc.
        # at the end

        # no that is incorrect, i want to store the numbers into the the index that corresponds to their
        # frequency.
        # i.e. if 1 shows up 3 times in the list it will be stored in index 3
        # therefore the frequency bucket list is len(nums) + 1 due to python being zero-indexed for simplicity

        # would have to loop through the list once to map their frequencies
        # traverse the map next and use their frequency as the index for the frequency bucket list
        # once the nums are stored in the bucket we can traverse the bucket list backwards popping from
        # that list k times to retreive the k most frequent nums

        ans = []
        bucket = [[] for _ in range(len(nums) + 1)]
        frequency = {}

        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1

        for num, freq in frequency.items():
            bucket[freq].append(num)
        
        for i in range(len(bucket) - 1, 0, -1):
            while len(bucket[i]) > 0:
                ans.append(bucket[i].pop())
                if len(ans) == k:
                    return ans

        
