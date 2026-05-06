class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # to validate the sudoku board in an efficient manner
        # and do it in a single traversal, we must keep track of
        # the rows, columns and boxes as we check each individual
        # box. after the box is checked and confirmed that it has
        # not been seen in any row, column or in its own box, we 
        # can add it to its corresponding row, column and box
        #
        # we can use a hashmap of sets to record the occurence of 
        # numbers in the board, where the key for each hashmap goes
        # as follows:
        # rows: row index
        # column: column index
        # box: tuple containing row//3, column//3
        #
        # the reason the key for the box is the row and the column //3 
        # is because each box is a 3x3 square and once we get to the next
        # box it will go to the next number, which creates a graph of boxes
        # essentially where their location is defined by their row and column
        # point.

        row = defaultdict(set)
        column = defaultdict(set)
        box = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue

                if (
                     board[r][c] in row[r] or
                     board[r][c] in column[c] or
                     board[r][c] in box[(r//3,c//3)]
                   ):
                   return False
                row[r].add(board[r][c])
                column[c].add(board[r][c])
                box[(r//3,c//3)].add(board[r][c])
        return True







