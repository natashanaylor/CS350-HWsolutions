
# CS 350: Homework 8
# Due: Week of 6/2
# Name: Natasha Naylor


################################################################
# Sudoku
#
# Sudoku is a game played on a 9x9 grid.
# You are given a partially filled in grid
# and there are 3 rules
# 1. no number can appear twice in the same row
# 2. no number can appear twice in the same column
# 3. no number can appear twice in the same 3x3 grid
#
# You need to write a function that takes in a sudoku board
# and return a solved sudoku board.
#
# example:
# +---+---+---+
# |   |26 |7 1|
# |68 | 7 | 9 |
# |19 |  4|5  |
# +---+---+---+
# |82 |1  | 4 |
# |  4|6 2|9  |
# | 5 |  3| 28|
# +---+---+---+
# |  9|3  | 74|
# | 4 | 5 | 36|
# |7 3| 18|   |
# +---+---+---+
#
# Solution:
# +---+---+---+
# |435|269|781|
# |682|571|491|
# |197|834|562|
# +---+---+---+
# |826|195|947|
# |374|682|915|
# |951|743|628|
# +---+---+---+
# |519|326|874|
# |248|957|136|
# |763|418|259|
# +---+---+---+

def sudoku(board):
    """
    >>> board = [ [4,3,0,2,6,0,7,0,1], \
                  [6,8,0,0,7,0,0,9,0], \
                  [0,0,0,0,0,4,5,0,0], \
                  [8,2,0,1,0,0,0,4,0], \
                  [0,0,4,6,0,2,9,0,0], \
                  [0,5,0,0,0,3,0,2,8], \
                  [0,0,9,3,0,0,0,7,4], \
                  [0,4,0,0,5,0,0,3,6], \
                  [7,0,3,0,1,8,0,0,0] ]
    >>> sudoku(board)
    [[4, 3, 5, 2, 6, 9, 7, 8, 1], [6, 8, 2, 5, 7, 1, 4, 9, 3], [1, 9, 7, 8, 3, 4, 5, 6, 2], [8, 2, 6, 1, 9, 5, 3, 4, 7], [3, 7, 4, 6, 8, 2, 9, 1, 5], [9, 5, 1, 7, 4, 3, 6, 2, 8], [5, 1, 9, 3, 2, 6, 8, 7, 4], [2, 4, 8, 9, 5, 7, 1, 3, 6], [7, 6, 3, 4, 1, 8, 2, 5, 9]]
    """
    pass

    #pick the first empty (row, column) on the board to make an entry
    r, c = findNextEmptySpace(board)

    #if there are no empty spaces left, then the board is complete
    if r is None:
        return board

    #if the board is not complete, put in an entry between 1 and 9
    for entry in range(1, 10):
        if validEntry(board, r, c, entry):
            board[r][c] = entry
            #recursively call sudoku to place the next entry
            if sudoku(board):
                return board
        #if the entry isn't valid or was an incorrect entry, then backtrack to
        #try a different entry. Reset the entry to empty (0)
        board[r][c] = 0
    

#helper function to find the next empty space on the board
def findNextEmptySpace(board):
    #for each row and column in the board
    for r in range(9):
        for c in range(9):
            #if the current row/column is empty, then return this index as a tuple
            if board[r][c] == 0:
                return r, c
    
    #if the board is full, return a None tuple
    return None, None

#helper function to determine if entry at given row/column is valid based on Sudoku rules
def validEntry(board, r, c, entry):
    #check for valid row entry
    rEntries = board[r]
    if entry in rEntries:
        return False
    
    #check for valid column entry
    #create an empty list to represent the column entries
    cEntries = []
    for i in range(9):
        cEntries.append(board[i][c])
    if entry in cEntries:
        return False

    #check for valid 3x3 grid entry
    #determine which 3x3 grid to check for valid entry, based on the row/column:
    #floor divide the row and column indices by 3, then multiply this value by 3
    #to get the starting row and column of the 3x3 grid
    startR = (r // 3) * 3
    startC = (c // 3) * 3

    #iterate the 3x3 grid, starting at the row/column starting point until the
    #end of that grid (starting index + 3)
    for i in range(startR, startR + 3):
        for j in range(startC, startC + 3):
            if board[i][j] == entry:
                return False
    
    #if all tests pass, then the entry is valid
    return True

if __name__ == "__main__":
    import doctest
    doctest.testmod()
