class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columns = defaultdict(set)
        rows = defaultdict(set)
        boxes = defaultdict(set)
        for row in range(9):
            for column in range(9):
                val = board[row][column]
                if val == '.':
                    continue
                if (val in rows[row] or
                   val in columns[column] or
                   val in boxes[(row//3,column//3)]):
                   return False
                rows[row].add(val)
                columns[column].add(val)
                boxes[(row//3, column//3)].add(val)
        
        return True
        