import time

import constants as C
import pygame as p

class GameState():
    def __init__(self):
        '''
        self.board = [
            ["--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--"],
        ]
        '''
        self.board = self.createBoard()

    def createBoard(self):
        board = []
        for r in range(C.ROWS):
            l = []
            for c in range(C.COLS):
                l.append(C.BLANK_STRING)
            board.append(l)
        #print(board)
        return board

    def printBoard(self):
        for row in self.board:
            for cell in row:
                print(cell, end=" ")
            print()

    def getLastEmptyRow(self, col):
        #print(self.board)

        for row in reversed(range(C.ROWS)):
            if self.board[row][col] == C.BLANK_STRING:
                return row

    #def getHorizontalVictory(self, row, col):
        #for i in range(4):
            #if self.board[row][col]

    def Victory(self, activePlayer, screen):
        if self.horizontalVictory(activePlayer, screen):
            #time.sleep(10)
            return True
        elif self.verticalVictory(activePlayer):
            return True
        elif self.diagonalUpVictory(activePlayer):
            return True
        elif self.diagonalDownVictory(activePlayer):
            return True
        #for i in range(4):

            #print(board)
            #if board[activePlayer.row][activePlayer.col] == activePlayer.playerColor:
                #return "victory"

    def horizontalVictory(self, activePlayer, screen):
        for row in range(len(self.board)):
            for col in range(len(self.board)-3):
                #print(row, col)
                if self.board[row][col] == activePlayer.playerColor and self.board[row][col+1] == activePlayer.playerColor and self.board[row][col+2] == activePlayer.playerColor and self.board[row][col+3] == activePlayer.playerColor:
                    #time.sleep(10)
                    #p.draw.line(screen, p.color(activePlayer.playerColor), (100, 100), (500, 500), width=3)
                    print("victory ", activePlayer.playerColor)
                    return True

    def verticalVictory(self, activePlayer):
        for col in range(len(self.board)):
            for row in range(len(self.board)-3):
                #print(row, col)
                if self.board[row][col] == activePlayer.playerColor and self.board[row+1][col] == activePlayer.playerColor and self.board[row+2][col] == activePlayer.playerColor and self.board[row+3][col] == activePlayer.playerColor:
                    print("victory ", activePlayer.playerColor)
                    return True

    def diagonalUpVictory(self, activePlayer):
        for row in range(3, len(self.board)):
            for col in range(len(self.board) - 3):
                #print(row, col)
                if self.board[row][col] == activePlayer.playerColor and self.board[row-1][col+1] == activePlayer.playerColor and self.board[row-2][col+2] == activePlayer.playerColor and self.board[row-3][col+3] == activePlayer.playerColor:
                    print("victory ", activePlayer.playerColor)
                    return True

    def diagonalDownVictory(self, activePlayer):
        for col in range(len(self.board)-3):
            for row in range(len(self.board)-3):
                if self.board[row][col] == activePlayer.playerColor and self.board[row+1][col+1] == activePlayer.playerColor and self.board[row+2][col+2] == activePlayer.playerColor and self.board[row+3][col+3] == activePlayer.playerColor:
                    print("victory ", activePlayer.playerColor)
                    return True

class Player():

    def __init__(self, playerColor, active, row, col, moves):
        self.playerColor = playerColor
        self.active = True
        self.row = row
        self.col = col
        self.moves = 0

    def printPlayerProperties(self):
        print(self.active)
        print(self.playerColor)
        print(self.row, self.col)
        print(self.moves)
        print(" ******       *********      *******")






