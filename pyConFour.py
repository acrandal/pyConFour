#!/usr/bin/env python3
#
# Python Connect 4 (TM) Terminal Game
#
# Simple non-object oriented solution.
#
# @author Aaron S. Crandall <crandall@gonzaga.edu>
# @copyright 2022
# @license GPL v3.0
#

from asyncore import ExitNow


g_board = []  # Global 2D list of lists
MAX_X = 7  # Game is 7 columns wide
MAX_Y = 6  # Game is 6 rows tall

tokens = ("X", "O")  # Player 1 is X, Player 2 is O


def buildBoard(board):
    for x in range(MAX_X):
        board.append([])
        for y in range(MAX_Y):
            board[x].append(" ")


def showBoard(board):
    print(" 0 1 2 3 4 5 6 ")
    print("|-------------|")
    for y in range(MAX_Y):
        print("|", end="")
        for x in range(MAX_X):
            print(board[x][y] + "|", end="")
        print("\n|-------------|")


def dropToken(board, token, columnIndex):
    print(f"Dropping token {token} at {columnIndex}")
    finalY = 0
    for y in range(MAX_Y):
        if board[columnIndex][y] == " ":
            finalY = y
    board[columnIndex][finalY] = token


def takeTurn(board, token):
    successfulDrop = False
    while not successfulDrop:
        showBoard(board)
        userInput = input(f"Which column do you drop your token {token} [0..6]? : ")
        if userInput == "q":
            raise ExitNow
        try:
            columnIndex = int(userInput)
            if not (0 <= columnIndex <= MAX_X):
                print("That is not a valid column choice.")
                continue
            elif board[columnIndex][0] != " ":
                print("That column is already full, select another")
                continue
            dropToken(board, token, columnIndex)
            successfulDrop = True
        except:
            print("Invalid choice, please try again")


def isFourHorizontals(board):
    for y in range(MAX_Y):
        for x in range(MAX_X - 3):
            possibleWinToken = board[x][y]
            if possibleWinToken == " ":
                pass  # Empty location, no win here
            elif (
                board[x + 1][y] == possibleWinToken
                and board[x + 2][y] == possibleWinToken
                and board[x + 3][y] == possibleWinToken
            ):
                return possibleWinToken
            else:
                pass  # No winner here
    return "-"


def isFourVerticals(board):
    for y in range(MAX_Y - 3):
        for x in range(MAX_X):
            possibleWinToken = board[x][y]
            if possibleWinToken == " ":
                pass  # Empty location, no win here
            elif (
                board[x][y + 1] == possibleWinToken
                and board[x][y + 2] == possibleWinToken
                and board[x][y + 3] == possibleWinToken
            ):
                return possibleWinToken
            else:
                pass  # No winner here
    return "-"


def isFourSlashes(board):
    for y in range(3, MAX_Y):
        for x in range(MAX_X - 3):
            possibleWinToken = board[x][y]
            if possibleWinToken == " ":
                pass  # Empty location, no win here
            elif (
                board[x + 1][y - 1] == possibleWinToken
                and board[x + 2][y - 2] == possibleWinToken
                and board[x + 3][y - 3] == possibleWinToken
            ):
                return possibleWinToken
            else:
                pass  # No winner here
    return "-"


def isFourBackslashes(board):
    for y in range(3, MAX_Y):
        for x in range(3, MAX_X):
            possibleWinToken = board[x][y]
            if possibleWinToken == " ":
                pass  # Empty location, no win here
            elif (
                board[x - 1][y - 1] == possibleWinToken
                and board[x - 2][y - 2] == possibleWinToken
                and board[x - 3][y - 3] == possibleWinToken
            ):
                return possibleWinToken
            else:
                pass  # No winner here
    return "-"


def isFourTie(board):
    for x in range(MAX_X):
        if board[x][0] == " ":
            return "-"
    return "T"


def isFour(board):
    # winState = "-"   # X, O, -, T (tie)
    # check horizontals -
    # check verticals   |
    # check slashes     /
    # check backslashes \
    # check tie
    if isFourHorizontals(board) in tokens:
        return isFourHorizontals(board)
    if isFourVerticals(board) in tokens:
        return isFourVerticals(board)
    if isFourSlashes(board) in tokens:
        return isFourSlashes(board)
    if isFourBackslashes(board) in tokens:
        return isFourBackslashes(board)
    if isFourTie(board) == "T":
        return "T"

    return "-"


def main(board):
    buildBoard(board)
    gameOver = False
    turnNumber = 0
    while not gameOver:
        currentToken = tokens[turnNumber % 2]
        takeTurn(board, currentToken)
        winState = isFour(board)
        # print("Win State: " + winState)

        if winState in tokens:
            showBoard(board)
            print(f"\nConnect 4 for {winState}!!!!")
            gameOver = True
        elif winState == "T":
            print("Tie game?")
            gameOver = True

        turnNumber += 1


if __name__ == "__main__":
    print("Playing Connect 4")
    try:
        main(g_board)
    except ExitNow:
        pass
    print("\nGame over.")
