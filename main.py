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

def switchPlayer(redPlayer, yellowPlayer):
    if redPlayer.active:
        redPlayer.active = False
        yellowPlayer.active = True
            #getActivePlayer(redPlayer, yellowPlayer).playerColor == 'red':
    else:
        redPlayer.active = True
        yellowPlayer.active = False

    return redPlayer, yellowPlayer


def drawGrid(screen):
    # draw vertical lines

    #connect4Engine.GameState
    for col in range(0, c.VERTICAL_LINE):
        p.draw.line(screen, p.Color("white"), (c.Xcoor, 100), (c.Xcoor, c.HEIGHT), width=3)
        c.Xcoor += 99

    # draw horizontal lines
    for row in range(0, 7):
        p.draw.line(screen, p.Color("white"), (2, c.Ycoor), (c.HEIGHT-5, c.Ycoor), width=3)
        c.Ycoor += 100

def drawCircle(screen, activePlayer, row, col):
    if activePlayer.playerColor == "red":
        if row > 0:
            p.draw.circle(screen, "red", ((col * 100)+50, (row * 100)+50), 45, width=10)
            activePlayer.moves += 1
            print(activePlayer.moves, " redPlayerCount ")


    #print(ce.board)
    elif activePlayer.playerColor == "yellow":
        if row > 0:
            p.draw.circle(screen, "yellow", ((col * 100)+50, (row * 100)+50), 45, width=10)
            activePlayer.moves += 1
            print(activePlayer.moves, " yellowPlayerCount ")
    #print(yc, " yc")

    #playerTurn(red, yellow, row, col)





def main():
    p.init()
    screen = p.display.set_mode((c.WIDTH, c.HEIGHT))
    # clock = p.time.Clock()
    screen.fill(p.Color("black"))
    drawGrid(screen)
    p.display.flip()
    running = True
    arena = ce.GameState()
    board = arena.board

    #print(board)
    redPlayer = ce.Player("red", True, 0, 0, 0)
    yellowPlayer = ce.Player("yellow", False, 0, 0, 0)

    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:
                # if not gameOver:  # uncomment when playing two player
                location = p.mouse.get_pos()


                activePlayer = getActivePlayer(redPlayer, yellowPlayer)
                row = activePlayer.row = location[1]//100
                col = activePlayer.col = location[0]//100
                emptyRow = arena.getLastEmptyRow(col)
                #print(emptyRow, " emptyRow")



                #if board[row][col] == "--":
                #if activePlayer.playerColor == "red":
                    #print(activePlayer.active, " active")
                #elif activePlayer.playerColor == "yellow":
                #drawCircle(screen, activePlayer, emptyRow, col)

                if emptyRow < 1:
                    redPlayer, yellowPlayer = switchPlayer(redPlayer, yellowPlayer)
                else:
                    drawCircle(screen, activePlayer, emptyRow, col)
                    board[emptyRow][col] = activePlayer.playerColor

                #print(board)
                    #print(activePlayer.active, " active")

                arena.printBoard()

                if arena.Victory(activePlayer, screen):
                    text = ("The winner is " + activePlayer.playerColor + "!!!")
                    drawText(screen, text, activePlayer)
                    time.sleep(20)

                    running = False


                redPlayer, yellowPlayer = switchPlayer(redPlayer, yellowPlayer)
                ce.Player.printPlayerProperties(redPlayer)
                ce.Player.printPlayerProperties(yellowPlayer)
                p.display.flip()
                #print(switchPlayer(redPlayer, yellowPlayer).playerColor, " switchPlayer")
                #activePlayer = switch

    #time.sleep(10)

    #clock.tick(MAX_FPS)

def animateMove():
    pass

def drawText(screen, text, activePlayer):
    winnerFont = p.font.SysFont("Times New Roman", 32, True, False)
    to = winnerFont.render(text, 0, p.Color("black"))
    textLocation = p.Rect(0, -300, c.WIDTH, c.HEIGHT).move(c.WIDTH/2 - to.get_width()/2, c.HEIGHT/2 - to.get_height()/2)
    screen.blit(to, textLocation)
    textObject = winnerFont.render(text, 0, p.Color(activePlayer.playerColor))
    screen.blit(textObject, textLocation.move(2, 2))


if __name__ == "__main__":
    main()


