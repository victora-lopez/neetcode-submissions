class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        row = 0
        while l <= r:
            row = l + (r - l) // 2
            if matrix[row][0] > target:
                r = row - 1
            elif matrix[row][-1] < target:
                l = row + 1
            else:
                break
        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            mid = l + (r-l)//2
            if matrix[row][mid] > target:
                r = mid - 1
            elif matrix[row][mid] < target:
                l = mid + 1
            else:
                return True
        return False
            