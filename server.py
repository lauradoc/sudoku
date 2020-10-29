import argparse
from tkinter import Tk, Canvas, Frame, Button, BOTH, TOP, BOTTOM

BOARDS = ['debug', 'n00b', 'l33t', 'error']  # Available sudoku boards
MARGIN = 20  # Pixels around the board
SIDE = 50  # Width of every board cell.
WIDTH = HEIGHT = MARGIN * 2 + SIDE * 9  # Width and height of the whole board

class SudokuError(Exception):
    """
    An application specific error.
    """
    pass


class SudokuBoard(object):
    """
    Sudoku Board representation
    """
    def __init__(self, board_file):
        self.board = __create_board(board_file)

    def __create_board(self, board_file):
        # create an initial matrix, or list of a list
        board = []

        # iterate over each line
        for line in board_file:
            line = line.strip()
            
            # Raise an error if there are not nine lines
            if len(line) != 9:
                board = []
                raise SudokuError(
                    "Each line in the sudoku puzzle must be 9 chars long"
            )

            # create a list for the line
            board.append([])

            # then iterate over each character
            for c in line:
                # Raise an error if the character is not an integer
                if not c.isdigit():
                    raise SudokuError(
                        "Valide characters for a sudoku puzzle must be 0-9"
                    )
                # Add to the latest list for the line
                board[-1].append(int(c))

        # Raise an error is there are not 9 lines
        if len(board) != 9:
            raise SudokuError("Each sudoku puzzle must be 9 lines long")

        # Return constructed board
        return board


class SudokuGame(object):
    """
    A Sudoku game, in charge of storing the state of the board and checking whether the puzzle is completed.
    """
    def __init__(self, board_file):
        self.board_file = board_file
        self.start_puzzle = SudokuBoard(board_file).board
    
    def start(self):
        self.game_over = False
        self.start_puzzle = []
        for i in xrange(9):
            self.puzzle.append([])
            for j in xrange(9):
                self.puzzle[i].append(self.start_puzzle[i][j])




# import random

# def load_puzzle():
#     """Function to load board to be solved. The puzzle represents 3x3 elements, 
#     3 across, 3 down. There should be nine lines of nine numbers 1-9 separated by commas.
#     Blank spaces are represented by 0's"""
    
#     board = [[0 for x in range(9)] for y in range(9)]

#     # for i in range(9):
#     #     for j in range(9):
#     #         board[i][j] = 0
   
#     display_puzzle(board)

#     # for i in range(9):
#     #     num = random.randrange(1,10)
#     #     row = random.randrange(9)
#     #     col = random.randrange(9)
#     #     while not CheckValid(board, row, col, num) or board[row][col] != 0:
#     #         num = random.randrange(1,10)
#     #         row = random.randrange(9)
#     #         col = random.randrange(9)
        
#     #     board[row][col] = num

#     for i in range(20):



# def display_puzzle(board):
#     top = "|--------------------------------|"
#     mid = "|----------+----------+----------|"

#     print(top)
#     for x in range(9):
#         for y in range(9):
#             if ((x == 3 or x == 6) and y == 0):
#                 print(mid)
#             if (y == 0 or y == 3 or y == 6):
#                 print("|", end=" ")
#             print(" " + str(board[x][y]), end=" ")
#             if y == 8:
#                 print("|")

#     print(top)

# # def CheckValid(board, row, col, num):

# #     for y in range(9):
# #         for x in range(9):



# load_puzzle()

