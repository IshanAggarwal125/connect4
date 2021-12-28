import time

import constants as C
import pygame as p
import random

class GameState():
    def __init__(self):
        self.board = self.createBoard()

    def createBoard(self):
        # Draw vertical and horizontal lines.
        board = []
        for r in range(C.ROWS):
            arr = []
            for c in range(C.COLS):
                arr.append(C.BLANK_STRING)
            board.append(arr)
        #print(board)
        return board

    def printBoard(self):
        # prints the 2D array on console.
        for row in self.board:
            for cell in row:
                print(cell, end=" ")
            print()

    def getLastEmptyRow(self, col):
        #print(self.board)
        print("getLastEmptyRow above for loop", col)
        for row in reversed(range(C.ROWS)):
            if self.board[row][col] == C.BLANK_STRING:
                print("getLastEmptyRow ", row)
                return row
        return -1

    #def getHorizontalVictory(self, row, col):
        #for i in range(4):
            #if self.board[row][col]

    def Victory(self, activePlayer, screen=None):
        if self.horizontalVictory(activePlayer, screen):
            return True
        elif self.verticalVictory(activePlayer, screen):
            return True
        elif self.diagonalUpVictory(activePlayer, screen):
            return True
        elif self.diagonalDownVictory(activePlayer, screen):
            return True
        return False


    def horizontalVictory(self, activePlayer, screen=None):
        for row in range(len(self.board)):
            for col in range(len(self.board)-3):
                #print(row, col)
                if self.board[row][col] == activePlayer.playerColor and self.board[row][col+1] == activePlayer.playerColor and self.board[row][col+2] == activePlayer.playerColor and self.board[row][col+3] == activePlayer.playerColor:
                    #time.sleep(10)
                    #p.draw.line(screen, p.color(activePlayer.playerColor), (100, 100), (500, 500), width=3)
                    print("victory", activePlayer.playerColor)
                    #p.display.flip()
                    if screen is not None:
                        p.draw.line(screen, p.Color("purple"), ((col*100)+50, (row*100)+50), (((col+3)*100)+50, (row*100)+50), width=5)
                    print(row, col, row, col+3, "victory coordinates")
                    return True

    def verticalVictory(self, activePlayer, screen=None):
        for col in range(len(self.board)):
            for row in range(len(self.board)-3):
                #print(row, col)
                if self.board[row][col] == activePlayer.playerColor and self.board[row+1][col] == activePlayer.playerColor and self.board[row+2][col] == activePlayer.playerColor and self.board[row+3][col] == activePlayer.playerColor:
                    if screen is not None:
                        p.draw.line(screen, p.Color("white"), ((col*100)+50, (row*100)+50), ((col*100)+50, ((row+3)*100)+50), width=5)
                    print("victory ", activePlayer.playerColor)
                    print(row, col, row+3, col, "victory coordinates")

                    return True

    def diagonalUpVictory(self, activePlayer, screen=None):
        for row in range(3, len(self.board)):
            for col in range(len(self.board) - 3):
                #print(row, col)
                if self.board[row][col] == activePlayer.playerColor and self.board[row-1][col+1] == activePlayer.playerColor and self.board[row-2][col+2] == activePlayer.playerColor and self.board[row-3][col+3] == activePlayer.playerColor:
                    if screen is not None:
                        p.draw.line(screen, p.Color("white"), ((col*100)+50, (row*100)+50), (((col+3)*100)+50, ((row-3)*100)+50), width=5)
                    print("victory ", activePlayer.playerColor)
                    print(row, col, row-3, col+3, "victory coordinates")
                    return True

    def diagonalDownVictory(self, activePlayer, screen=None):
        for col in range(len(self.board)-3):
            for row in range(len(self.board)-3):
                if self.board[row][col] == activePlayer.playerColor and self.board[row+1][col+1] == activePlayer.playerColor and self.board[row+2][col+2] == activePlayer.playerColor and self.board[row+3][col+3] == activePlayer.playerColor:
                    if screen is not None:
                        p.draw.line(screen, p.Color("white"), ((col*100)+50, (row*100)+50), (((col+3)*100)+50, ((row+3)*100)+50), width=5)
                    print("victory ", activePlayer.playerColor)
                    print(row, col, row+3, col+3, "victory coordinates")

                    return True




class Player():

    def __init__(self, playerColor, active, moves):
        self.playerColor = playerColor
        self.active = True
        #self.row = row
        #self.col = col
        self.moves = 0

    def printPlayerProperties(self):
        print(self.active)
        print(self.playerColor)
        print(self.row, self.col)
        print(self.moves)
        print(" ******       *********      *******")


    def getRandomRowCol(self):
        row = random.randint(1, 6)
        col = random.randint(0, 6)
        return row, col


    def finalRandomRowAndCol(self, arena):
        while True:
            # row, col = getFinalRowCol(row, col)
            row, col = self.getRandomRowCol()
            row = arena.getLastEmptyRow(col)
            if row > 0:
                break
        return row, col


    def aiRandomRowAndCol(self, arena, activePlayer):
        newArena = self.copyArena(arena)
        newPlayer = self.copyPlayer(activePlayer)
        count = 0
        max = 5
        while count < max:
            count += 1
            win, col = self.calculateVictoryForAllColumns(newArena, newPlayer)
            if not win:
                row, col = self.finalRandomRowAndCol(newArena)
                newArena.board[row][col] = newPlayer.playerColor
                print(newArena.printBoard())
                newPlayer = self.switchPlayer()
            else:
                break

        if count == max:
            print(max, " max", row, col)
            row, col = self.finalRandomRowAndCol(arena)
        else:
            row = arena.getLastEmptyRow(col)
        print("ai row col ", row,col)

        return row, col

    def calculateVictoryForAllColumns(self, newArena, activePlayer):
        print(activePlayer.playerColor)
        for col in range(0, C.HORIZONTAL_LINE):
            row = newArena.getLastEmptyRow(col)
            if row == -1:
                continue
            newArena.board[row][col] = activePlayer.playerColor
            if newArena.Victory(activePlayer):
                return True, col
            else:
                newArena.board[row][col] = C.BLANK_STRING
        print(newArena.printBoard())
        return False, col

    def copyArena(self, arena):
        newArena = GameState()
        for row in range(0, C.HORIZONTAL_LINE):
            for col in range(0, C.HORIZONTAL_LINE):
                newArena.board[row][col] = arena.board[row][col]
        return newArena

    def copyPlayer(self, activePlayer):
        return Player(activePlayer.playerColor, True, 0)

    '''
    def switchPlayer(self, redPlayer, yellowPlayer):
        if redPlayer.active:
            redPlayer.active = False
            yellowPlayer.active = True
            # getActivePlayer(redPlayer, yellowPlayer).playerColor == 'red':
        else:
            redPlayer.active = True
            yellowPlayer.active = False

        return redPlayer, yellowPlayer

    '''

    def switchPlayer(self):
        if self.playerColor == "red":
            self.playerColor = "yellow"
            self.active = True
            return self
        else:
            self.playerColor = "red"
            self.active = True
            return self




class button():
    def __init__(self, color, xCoor, yCoor, width, height, text=""):
        self.color = color
        self.xCoor = xCoor
        self.yCoor = yCoor
        self.width = width
        self.height = height
        self.text = text

    def drawButton(self, screen):
        p.draw.rect(screen, self.color, (self.xCoor, self.yCoor, self.width, self.height), 0)
        if self.text != "":
            Font = p.font.SysFont("Times New Roman", 40)
            to = Font.render(self.text, 1, p.Color("black"))
            #textLocation = p.Rect(0, -300, C.WIDTH, C.HEIGHT).move(C.WIDTH / 2 - to.get_width() / 2, C.HEIGHT / 2 - to.get_height() / 2)
            #screen.blit(to, textLocation)
            #textObject = Font.render(self.text, 0, p.Color("white"))
            screen.blit(to, (self.xCoor + (self.width/2 - to.get_width()/2), self.yCoor + (self.height/2 + to.get_height()/2 -50)))
        return

    def mousePosition(self, position):
        row = position[0]
        col = position[1]
        if self.xCoor < row < self.xCoor + self.width:
            if self.yCoor < col < self.yCoor + self.height:
                return True
        return False










