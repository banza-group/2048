"""Engine with the game rules."""
import block as b
import random
import numpy as np

# Variables used to generate random values
randomValuesOne = [0, 0, 0, 0, 0, 0, 0, 2, 2, 4]
randomValuesTwo = [0, 0, 0, 0, 0, 0, 0, 2, 2, 4]


def createBoard(size):
    """Create the board."""
    board = list()
    for i in range(size):
        line = list()
        for j in range(size):
            line.append(b.Block(random.choice(randomValuesTwo)))
        board.append(line)
    return board


def move(direction, board):
    """Move the numbers in determined direction."""
    direction = str(direction).upper()
    if direction == "L":
        moveLeft(board)
    elif direction == "R":
        moveRight(board)
    elif direction == "U":
        moveUp(board)
    elif direction == "D":
        moveDown(board)


def addRandomValuesBoard(board):
    """Add random item values in the board."""
    count = 0
    for i in range(len(board)):
        line = board[i]
        for j in range(len(line)):
            if line[j].value == 0 and count < 2:
                line[j].value = random.choice(randomValuesOne)
                count += 1


def showBoard(board):
    """Show the board values.

    Change 2D array with Block items into a 2D array with int values.
    """
    boardN = list()
    for i in range(len(board)):
        line = board[i]
        lineN = list()
        for j in line:
            lineN.append(j.value)
        boardN.append(lineN)
    return boardN


def moveRight(board):
    """Move to right."""
    oldBoard = list(board)
    for i in range(len(board)):
        board[i] = sumLineRight(orderLineRight(board[i]))
    npOldBoard = np.array(showBoard(oldBoard))
    npBoard = np.array(showBoard(board))
    """Compare the old and new board to verify any differences
    If there are no differences, the random values will not be insertself.
    If there are diffenreces, the random values will be insert.
    """
    print("oldBoard: {}".format(showBoard(oldBoard)))
    print("board: {}".format(showBoard(board)))
    if np.array_equal(npOldBoard, npBoard) is False:
        print(">>> DIFFERENT")
        addRandomValuesBoard(board)
    else:
        print(">>> EQUAL")


def moveLeft(board):
    """Move to left."""
    invertBoard(board)
    moveRight(board)
    invertBoard(board)


def moveUp(board):
    """Move upward."""
    rotateBoardRight(board)
    moveRight(board)
    rotateBoardRight(board)
    rotateBoardRight(board)
    rotateBoardRight(board)


def moveDown(board):
    """Move downward."""
    rotateBoardRight(board)
    rotateBoardRight(board)
    rotateBoardRight(board)
    moveRight(board)
    rotateBoardRight(board)


def orderLineRight(line):
    """Order to be right aligned."""
    lineN = list()
    for i in range(len(line)):
        if line[i].value != 0:
            lineN.append(line[i])
    if len(lineN) != len(line):
        while len(lineN) < len(line):
            lineN.insert(0, b.Block(0))
    return lineN


def sumLineRight(line):
    """Sum right aligned line values."""
    for i in reversed(range(len(line))):
        if i-1 >= 0:
            if line[i].value == line[i-1].value:
                # sum
                line[i].value = line[i].value + line[i-1].value
                # remove item
                del(line[i-1])
                # insert empty item
                line.insert(0, b.Block(0))
    return line


def rotateBoardRight(board):
    """Rotate board 45 degrees to right."""
    npList = list()
    # create a list of numpy array items
    for i in range(len(board)):
        npList.append(np.array(board[i]))
    # change line to columns
    changedList = np.column_stack((npList[::-1]))
    # set original board list with the new values
    for i in range(len(changedList)):
        board[i] = changedList[i]


def invertBoard(board):
    """Invert board values like a mirror."""
    for i in range(len(board)):
        board[i] = board[i][::-1]
