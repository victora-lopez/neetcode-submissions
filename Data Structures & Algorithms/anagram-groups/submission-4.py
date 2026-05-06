class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for s in strs:
            key = sorted(s)
            key = tuple(key)
            ans[key].append(s)
        
        return ans.values();
