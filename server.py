import random

def load_puzzle():
    """Function to load board with to be solved. The puzzle represents 3x3 elements, 
    3 across, 3 down. There should be nine lines of nine numbers 0-9 separated by commas."""
    
    board = [[0 for x in range(9)] for y in range(9)]

    for i in range(9):
        for j in range(9):
            board[i][j] = 0
    # fileHandle = open("board.txt")
    # puzzle = fileHandle.readlines()
    # for line in range(len(puzzle)):
    #     board.append
    
    # while len(board) < 10:
    #     num = randint(1,9)
    #     if num not in board:
    #         board.append(num)

    #     if len(board) == 9 or 18 or 27 or 36 or 45 or 54 or 63 or 72:
    #         n
    display_unsolved_puzzle(board)

def display_unsolved_puzzle(board):
    top = "|----------------------------|"
    middle = "|-------+----------+---------|"

    print(top)
    for x in range(9):
        for y in range(9):
            if (x % 3 == 0):
                print("|")
            print(" " + board[x][y] + " ")

load_puzzle()


# def autofill_puzzle():
