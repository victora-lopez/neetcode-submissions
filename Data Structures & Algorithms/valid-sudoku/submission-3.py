class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columns = [0] * 9
        rows = [0] * 9
        boxes = [0] * 9

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue

                value = 1 << (int(board[r][c]) - 1)

                if rows[r] & value:
                    return False
                if columns[c] & value:
                    return False
                if boxes[r//3 * 3 + c//3] & value:
                    return False
                
                rows[r] |= value
                columns[c] |= value
                boxes[r//3 * 3 + c//3] |= value
        return True