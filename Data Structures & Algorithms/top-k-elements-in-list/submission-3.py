class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums)+1)]
        ans = []

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        for num,c in count.items():
            freq[c].append(num)
        
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans
                    
