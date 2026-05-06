class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # we want to group each row, column and box into its own respective groups
        # and store them in sets for constant time retrieval
        # the reason we want to store number we are currently on into its r,c and box
        # is because we want to check when we move to future boxes if we have seen that number
        # in that r,c or box
        # 
        # for the boxes we can store it like a coordinate system where we do integer divison
        # on the row and column by 3 since the boxes are 3x3
        # 
        # with this the pieces for writing the code should be straight forward
        #
        # input: board as a list of strings
        # output: True or False if it is valid or not

        row = defaultdict(set)
        column = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (
                    board[r][c] in row[r] or
                    board[r][c] in column[c] or
                    board[r][c] in boxes[(r // 3, c // 3)]
                   ):
                   return False
                row[r].add(board[r][c])
                column[c].add(board[r][c])
                boxes[r // 3, c // 3].add(board[r][c])
        return True