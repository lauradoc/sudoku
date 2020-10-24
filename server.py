import argparse
from Tkinter import Tk, Canvas, Frame, Button, BOTH, TOP, BOTTOM






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

