from sudoku import Sudoku 
import random   

puzzle = Sudoku(3).difficulty(0.5)
puzzle.show()
solution=puzzle.solve()
solution.show()
# #loop over the solution boards[0]
# for i in range (9):
print(solution.board)
    # right_numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9]
    # if solution.board == right_numbers:
    #     print("correct")
    # else:
    #     print("Try Again")
    
    # With solution board create a def called repeated_numbers that just print the numbers that are not supossed to be in each list. 
    #print(Sudoku.index)