class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r = 0, len(numbers) - 1

        while l < r:
            complement = numbers[l] + numbers[r]
            if complement > target:
                # complement is too large so move right pointer down
                r -= 1
            elif complement < target:
                # complement is too small so move left pointer up
                l += 1
            if complement == target:
                return [l + 1, r + 1]