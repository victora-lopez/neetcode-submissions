class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int complement;
        int n = nums.size();
        unordered_map<int,int> seen;
        
        for(int i = 0; i<n; i++){
            complement = target - nums[i];
            if(seen.find(complement) != seen.end())
                return{seen[complement],i};
            seen.insert({nums[i],i});
        }
        return {};
    }
};
