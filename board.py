#With board.py create a board totally solved and take the result to replace board on final.py to validate the board.

from sudoku import Sudoku 
import random   

puzzle = Sudoku(3).difficulty(0.5)
puzzle.show()
solution=puzzle.solve()
solution.show()
print(solution.board)
    