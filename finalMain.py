# connect 4
import pygame as p
import connect4Engine as ce
import constants as c
import time


MAX_FPS = 15

def getActivePlayer(redPlayer, yellowPlayer):
    if redPlayer.active:
        return redPlayer
    else:
        return yellowPlayer


def drawGrid(screen):
    # draw vertical lines
    print("drawGrid", screen)
    #connect4Engine.GameState
    for col in range(0, c.VERTICAL_LINE):
        p.draw.line(screen, p.Color("blue"), (c.Xcoor, 100), (c.Xcoor, c.HEIGHT), width=5)
        c.Xcoor += 99
        #p.display.flip()

    # draw horizontal lines
    for row in range(0, 7):
        p.draw.line(screen, p.Color("blue"), (2, c.Ycoor), (c.HEIGHT-5, c.Ycoor), width=5)
        c.Ycoor += 100
        #p.display.flip()

    #time.sleep(3)
    return

def drawCircle(screen, activePlayer, row, col):
    if activePlayer.playerColor == "red":
        #if row > 0:
        p.draw.circle(screen, "red", ((col * 100)+50, (row * 100)+50), 45, width=0)
        p.draw.circle(screen, "white", ((col * 100)+50, (row * 100)+50), 45, width=3)

        #activePlayer.moves += 1
        #print(activePlayer.moves, " redPlayerCount ")


    #print(ce.board)
    elif activePlayer.playerColor == "yellow":
        #if row > 0:
        p.draw.circle(screen, "yellow", ((col * 100)+50, (row * 100)+50), 45, width=0)
        p.draw.circle(screen, "white", ((col * 100)+50, (row * 100)+50), 45, width=3)

        #activePlayer.moves += 1
        #print(activePlayer.moves, " yellowPlayerCount ")
    #print(yc, " yc")

    #playerTurn(red, yellow, row, col)



def howToPlayScreen(screen):

    initializeHowToPlayScreen(screen)
    text1 = "The goal of the game is to get 4 coins in a row."
    text2 = "This can be done vertically, horizontally, or diagonally."
    text3 = "Here are some examples of a victory."
    drawTextBasedOnDimensions(screen, text1, -240, "yellow")
    drawTextBasedOnDimensions(screen, text2, -190, "yellow")
    drawTextBasedOnDimensions(screen, text3, -140, "yellow")

    vertVic = p.image.load(r"verticalVictory.png")
    screen.blit(vertVic, (20, 250))
    horVic = p.image.load(r"horizontalVictory.png")
    screen.blit(horVic, (150, 350))
    diagUpVic = p.image.load(r"diagonalUp.png")
    screen.blit(diagUpVic, (400, 200))
    diagDownVic = p.image.load(r"diagonalDown.png")
    screen.blit(diagDownVic, (400, 450))
    p.display.update()
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False

            if e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos()
                running = getBackButton(screen, location)

    return True
    #time.sleep(10)


def onePlayerBoard():
    arr = []
    for i in range(c.HORIZONTAL_LINE):
        arr.append([])
    return arr

def getCoordinatesAfterAi():
    pass

def onePlayerConnect4(screen):
    intitalizeBoard(screen)
    aiArray = onePlayerBoard()
    running = True
    arena = ce.GameState()
    board = arena.board

    redPlayer = ce.Player("red", True, 0)
    yellowPlayer = ce.Player("yellow", False, 0)

    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False

            if e.type == p.MOUSEBUTTONDOWN:
                # if not gameOver:  # uncomment when playing two player
                location = p.mouse.get_pos()

                activePlayer = getActivePlayer(redPlayer, yellowPlayer)

                #row = location[1] // 100
                col = location[0] // 100
                row = arena.getLastEmptyRow(col)

                if row >= 1:
                    color = getOppositeOfActivePlayer(activePlayer)
                    text = ("It is " + color + "'s turn.")
                    clearText(screen)
                    drawText(screen, text, color)
                    p.display.flip()

                    #if activePlayer.playerColor == "red":

                    if activePlayer.playerColor == "yellow":
                        row, col = yellowPlayer.aiRandomRowAndCol(arena, activePlayer)


                            #print(emptyRow, col, "computerMove")
                    drawCircle(screen, activePlayer, row, col)
                    activePlayer.moves += 1
                    board[row][col] = activePlayer.playerColor

                    if calculateVictory(arena, screen, activePlayer):
                        return True

                    if row >= 1:
                        activePlayer = activePlayer.switchPlayer()

                    # print(emptyRow, " emptyRow")

                    if redPlayer.moves == c.TOTAL_MOVES and yellowPlayer.moves == c.TOTAL_MOVES and not arena.Victory(activePlayer):
                        clearText(screen)
                        text = "The game is a draw!!!"
                        drawText(screen, text, "white")
                        p.display.flip()
                        time.sleep(10)
                        return True

                # print(board)
                # print(activePlayer.active, " active")
                print("Main board")
                arena.printBoard()



                p.display.flip()
                running = getBackButton(screen, location)

    return True


def startingScreen(isFirst):
    running = True
    #twoPlayerButton.mousePosition(location)
    displayScreenOptions = True

    while running:
        if displayScreenOptions:
            screen, twoPlayerButton, onePlayerButton, howToPlayButton = startingScreenOptions(isFirst)
            displayScreenOptions = False
            isFirst = False
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:
                # if not gameOver:  # uncomment when playing two player
                location = p.mouse.get_pos()

                if twoPlayerButton.mousePosition(location):
                    #mouseMovement()
                    displayScreenOptions = twoPlayerConnect4(screen)
                elif onePlayerButton.mousePosition(location):
                    displayScreenOptions = onePlayerConnect4(screen)
                elif howToPlayButton.mousePosition(location):
                    displayScreenOptions = howToPlayScreen(screen)

def startingScreenOptions(isFirst):
    print("startingScreenOptions ")
    if isFirst:
        p.init()

    screen = p.display.set_mode((c.WIDTH, c.HEIGHT))
    p.display.set_caption("connect 4")
        # clock = p.time.Clock()
    screen.fill(p.Color("black"))
    #p.display.flip()
    text = "Welcome to Connect 4"
    drawOtherText(screen, text)
    #p.display.flip()
    twoPlayerButton = ce.button(p.Color("Red"), 250, 250, c.WIDTH - 500, c.HEIGHT - 600, "Two Player")
    twoPlayerButton.drawButton(screen)
    howToPlayButton = ce.button(p.Color("yellow"), 250, 100, c.WIDTH - 500, c.HEIGHT - 600, "How to play")
    howToPlayButton.drawButton(screen)
    onePlayerButton = ce.button(p.Color("blue"), 250, 400, c.WIDTH - 500, c.HEIGHT - 600, "One player")
    onePlayerButton.drawButton(screen)
    # howToPlayButton = ce.button(p.Color())
    # position = p.mouse.get_pos()
    # print(position)
    # twoPlayerButton.mousePosition(position)
    p.display.flip()
    return screen, twoPlayerButton, onePlayerButton, howToPlayButton

def intitalizeBoard(screen):
    #p.init()
    #screen = p.display.set_mode((c.WIDTH, c.HEIGHT))
    # clock = p.time.Clock()
    screen.fill(p.Color("black"))
    backButton = ce.button(p.Color("Red"), c.BACK_X1, c.BACK_Y1, c.BACK_WIDTH, c.BACK_HEIGHT, "Back")
    backButton.drawButton(screen)

    drawGrid(screen)
    p.display.flip()
    return screen

def initializeHowToPlayScreen(screen):
    screen.fill(p.Color("black"))
    backButton = ce.button(p.Color("Red"), c.BACK_X1, c.BACK_Y1, c.BACK_WIDTH, c.BACK_HEIGHT, "Back")
    backButton.drawButton(screen)

    #drawGrid(screen)
    p.display.flip()
    return screen


def twoPlayerConnect4(screen):
    print("def twoPlayerConnect4")
    intitalizeBoard(screen)
    running = True
    arena = ce.GameState()
    board = arena.board

    redPlayer = ce.Player("red", True, 0)
    yellowPlayer = ce.Player("yellow", False, 0)

    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False

            if e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos()
                # if not gameOver:  # uncomment when playing two player


                activePlayer = getActivePlayer(redPlayer, yellowPlayer)

                print(redPlayer.playerColor, yellowPlayer.playerColor,activePlayer.playerColor)

                row = location[1] // 100
                col = location[0] // 100

                # print(row, col)
                emptyRow = arena.getLastEmptyRow(col)
                # print(emptyRow, " emptyRow")

                if emptyRow >= 1:
                    color = getOppositeOfActivePlayer(activePlayer)
                    text = ("It is " + color + "'s turn.")
                    clearText(screen)
                    drawText(screen, text, color)
                    p.display.flip()

                    drawCircle(screen, activePlayer, emptyRow, col)
                    activePlayer.moves += 1
                    print(activePlayer.playerColor, " Player color ")
                    board[emptyRow][col] = activePlayer.playerColor

                if calculateVictory(arena, screen, activePlayer):
                    return True

                if emptyRow >= 1:
                    activePlayer = activePlayer.switchPlayer()

                if redPlayer.moves == c.TOTAL_MOVES and yellowPlayer.moves == c.TOTAL_MOVES and not arena.Victory(activePlayer):
                    clearText(screen)
                    text = "The game is a draw!!!"
                    drawText(screen, text, "white")
                    p.display.flip()
                    time.sleep(10)
                    return True

                    #clock.tick(1)
                    #running = False

                # print(board)
                # print(activePlayer.active, " active")

                arena.printBoard()


                #text = ("It is " + activePlayer.playerColor + "'s turn.")
                #drawText(screen, text, activePlayer)
                # ce.Player.printPlayerProperties(redPlayer)
                # ce.Player.printPlayerProperties(yellowPlayer)
                p.display.flip()
                running = getBackButton(screen, location)
                print("back running", running)
                # print(switchPlayer(redPlayer, yellowPlayer).playerColor, " switchPlayer")
                # activePlayer = switch

    return True


def calculateVictory(arena, screen, activePlayer):
    if arena.Victory(activePlayer, screen):
        clearText(screen)
        text = ("The winner is " + activePlayer.playerColor + "!!!")
        drawText(screen, text, activePlayer.playerColor)
        p.display.flip()
        time.sleep(3)
        return True
    return False

def showCircle(screen, color, row, col):
    p.draw.circle(screen, color, ((col * 100) + 50, (row * 100) + 50), 45, width=0)
    p.draw.circle(screen, "white", ((col * 100) + 50, (row * 100) + 50), 45, width=3)



def main():
    #print(inputString("//hello"))
    startingScreen(True)


def getBackButton(screen, position):
    row = position[0]
    col = position[1]
    print(row, col, " back button")
    if c.BACK_X1 < row < c.BACK_X1 + c.BACK_WIDTH:
        if c.BACK_Y1 < col < c.BACK_Y1 + c.BACK_HEIGHT:
            return False
    return True


def clearText(screen):
    p.draw.rect(screen, p.Color("black"), (150, -605, c.WIDTH, c.HEIGHT))

def drawText(screen, text, color):
    winnerFont = p.font.SysFont("Times New Roman", 40, True, False)
    to = winnerFont.render(text, 0, p.Color("black"))
    textLocation = p.Rect(0, -300, c.WIDTH, c.HEIGHT).move(c.WIDTH/2 - to.get_width()/2, c.HEIGHT/2 - to.get_height()/2)
    screen.blit(to, textLocation)
    textObject = winnerFont.render(text, 0, p.Color(color))
    screen.blit(textObject, textLocation.move(2, 2))


def drawOtherText(screen, text):
    Font = p.font.SysFont("Times New Roman", 40, True, False)
    to = Font.render(text, 0, p.Color("black"))
    textLocation = p.Rect(0, -300, c.WIDTH, c.HEIGHT).move(c.WIDTH / 2 - to.get_width() / 2, c.HEIGHT / 2 - to.get_height()/2)
    screen.blit(to, textLocation)
    textObject = Font.render(text, 0, p.Color("white"))
    screen.blit(textObject, textLocation.move(2, 2))

def drawTextBasedOnDimensions(screen, text, location, color):
    Font = p.font.SysFont("Times New Roman", 30, True, False)
    to = Font.render(text, 0, p.Color("blue"))
    textLocation = p.Rect(0, location, c.WIDTH, c.HEIGHT).move(c.WIDTH / 2 - to.get_width() / 2,
                                                               ((c.HEIGHT / 2 - to.get_height() / 2)-30))
    screen.blit(to, textLocation)
    textObject = Font.render(text, 0, p.Color(color))
    screen.blit(textObject, textLocation.move(2, 2))


def getOppositeOfActivePlayer(activePlayer):
    if activePlayer.playerColor == "red":
        return "yellow"
    elif activePlayer.playerColor == "yellow":
        return "red"


if __name__ == "__main__":
    main()


