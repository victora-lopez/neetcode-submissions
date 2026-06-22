class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(A) > len(B):
            A, B = B, A
        
        l, r = 0, len(A) - 1

        while True:
            end_left_part_a = (l + r) // 2
            end_left_part_b = half - end_left_part_a - 2

            A_left = A[end_left_part_a] if end_left_part_a >= 0 else float('-infinity')
            A_right = A[end_left_part_a + 1] if end_left_part_a + 1 < len(A) else float('infinity')
            B_left = B[end_left_part_b] if end_left_part_b >= 0 else float('-infinity')
            B_right = B[end_left_part_b + 1] if end_left_part_b + 1 < len(B) else float('infinity')

            if (A_left <= B_right) and (B_left <= A_right):
                # correct partition found
                if total % 2:
                    return min(A_right, B_right)
                else:
                    return (min(A_right, B_right) + max(A_left, B_left)) / 2
            elif A_left > B_right:
                r = end_left_part_a - 1
            else:
                l = end_left_part_a + 1