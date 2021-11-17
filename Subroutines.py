import MineSweeper as Sweep
import tkinter as tk
import random
import time

def interact(tilex,tiley):
    global selectionMode
    if tilex < boardx and tiley < boardy and tilex > -1 and tiley > -1:
        if Sweep.selectionMode == "dig":
            dig(tilex,tiley)
        elif Sweep.selectionMode == "flag":
            flag(tilex,tiley)

def changeMode(mode):
    global selectionMode
    Sweep.selectionMode = mode

def gameSetup(difficulty): ## TODO Replace gameSetup() with GUI inputs
    global numberOfMines, boardx, boardy, gameRun, master
    isFirstMove = True
    gameRun = True
    if difficulty == "easy":
        boardx, boardy, numberOfMines = 10, 5, 10
    if difficulty == "normal":
        boardx, boardy, numberOfMines= 10, 5, 15
    if difficulty == "hard":
        boardx, boardy, numberOfMines= 10, 5, 25
    if difficulty == "custom":
        boardx, boardy, = 10, 5
        numberOfMines = int(input("number of mines: "))
    master = tk.Toplevel()
    master.title("Minesweeper")
    master.geometry("1000x600")
    shovelBtn = tk.Button(master, image = Sweep.imgArr[11],
                          command=lambda: changeMode("dig")
                          )
    shovelBtn.place(x=400, y=500)
    flagBtn = tk.Button(master, image = Sweep.imgArr[10],
                        command=lambda: changeMode("flag")
                        )
    flagBtn.place(x=500,y=500)
    boardGen()

def numberIncr(x,y):
    global hiddenBoard
    if hiddenBoard[x][y] == 9:
        hiddenBoard[x][y] = 1
    else:
        hiddenBoard[x][y] += 1
        
def number():
    global boardx, boardy, hiddenBoard, buttonList
    # For all tiles on board
    for x in range(0,boardx):
        for y in range(0,boardy):
            # If the tile is "safe"
            if hiddenBoard[x][y] != 0:
                hiddenBoard[x][y] = 9
                # NORTHWEST CORNER
                if x>0 and y>0 and hiddenBoard[x-1][y-1] == 0:
                    numberIncr(x,y)
                # NORTHEAST CORNER
                if x<boardx-1 and y>0 and hiddenBoard[x+1][y-1] == 0:
                    numberIncr(x,y)
                # SOUTHWEST CORNER
                if x>0 and y<boardy-1 and hiddenBoard[x-1][y+1] == 0:
                    numberIncr(x,y)
                # SOUTHEAST CORNER
                if x<boardx-1 and y<boardy-1 and  hiddenBoard[x+1][y+1] == 0:
                    numberIncr(x,y)
                # NORTH                        
                if y>0 and hiddenBoard[x][y-1] == 0:
                    numberIncr(x,y)
                # EAST
                if x<boardx-1 and hiddenBoard[x+1][y] == 0:
                    numberIncr(x,y)
                # SOUTH
                if y<boardy-1 and hiddenBoard[x][y+1] == 0:
                    numberIncr(x,y)
                # WEST
                if x>0 and hiddenBoard[x-1][y] == 0:
                    numberIncr(x,y)

            buttonList[x][y] = tk.Button(master, text=str(shownBoard[x][y]),
                                             command=lambda x=x, y=y: interact(x,y),
                                             width=13, height=6,
                                             bg="#f3f3f3", fg="#ffffff",
                                             activebackground='#999999')
            buttonList[x][y].place(x=x*100,y=y*100)

def boardGen():
    """
    Generates a shownBoard and buttonList, for the player to see and interact with.
    Generates a hiddenBoard, for the system to compare values
    and to copy across to the shownBoard when necessary.
    """
    global boardx, boardy, isFirstMove, hiddenBoard, shownBoard, buttonList
    hiddenBoard = [[9 for y in range(0,boardy)] for x in range(0,boardx)]
    shownBoard = [[None for y in range(0,boardy)] for x in range(0,boardx)]
    buttonList = [[None for y in range(0,boardy)] for x in range(0,boardx)]
    isFirstMove = True
    for x in range(0,boardx):
            for y in range(0,boardy):
                buttonList[x][y] = tk.Button(master, text=str(shownBoard[x][y]),
                                             command=lambda x=x, y=y: interact(x,y),
                                             width=13, height=6,
                                             bg="#f3f3f3", fg="#ffffff",
                                             activebackground='#999999')
                buttonList[x][y].place(x=x*100,y=y*100)

def dig(tilex,tiley):
    """
    Reveals the contents of the selected tile.
    If the tile is a mine, then the game is over and the player loses.
    """
    global isFirstMove, hiddenBoard, shownBoard, boardx, boardy, buttonList, numberOfMines
    if isFirstMove == True:
        remainingMines = numberOfMines
        randomx, randomy = int(tilex), int(tiley)

        """
        Deploys all mines on the board
        """
        while remainingMines > 0:
            if hiddenBoard[randomx][randomy] == 9 and (randomx < int(tilex-1) or randomy < int(tiley-1) or randomx > int(tilex+1) or randomy > int(tiley+1)):
                print("true")
                remainingMines -= 1
                hiddenBoard[randomx][randomy] = 0
            randomx, randomy, = random.randint(0,boardx-1), random.randint(0,boardy-1)
        number()
        buttonList = [[None for y in range(0,boardy)] for x in range(0,boardx)]
        for x in range(boardx):
            for y in range(boardy):
                buttonList[x][y] = tk.Button(master, text=str(shownBoard[x][y]),
                                             command=lambda x=x, y=y: interact(x,y),
                                             width=13, height=6,
                                             bg="#f3f3f3", fg="#ffffff",
                                             activebackground='#999999')
                buttonList[x][y].place(x=x*100,y=y*100)
        isFirstMove = False
    shownBoard[int(tilex)][int(tiley)] = hiddenBoard[int(tilex)][int(tiley)] # displays the hidden value on the board
    buttonList[tilex][tiley] = tk.Label(master, image=Sweep.imgArr[int(shownBoard[tilex][tiley])])
    buttonList[tilex][tiley].place(x=tilex*100, y=tiley*100)
    if hiddenBoard[int(tilex)][int(tiley)] == 0:
        gameOver()
    if hiddenBoard[int(tilex)][int(tiley)] == 9:
        groupClear()

def flag(tilex,tiley):
    """
    Marks the chosen tile as a flag.
    """
    global shownBoard, hiddenBoard
    if shownBoard[tilex][tiley]  == 10:
        shownBoard[tilex][tiley] = 14 ## ADD RESOURCE ##
    else:
        shownBoard[tilex][tiley] = 10
    buttonList[tilex][tiley] = tk.Button(master, image=Sweep.imgArr[int(shownBoard[tilex][tiley])], command=lambda x=tilex, y=tiley: interact(x,y))
    buttonList[tilex][tiley].place(x=tilex*100, y=tiley*100)

def groupClear():
    """
    Detects if there are any unrevealed tiles adjacent to a revealed, empty tile that are to be revealed,
    and then reveals them to the player.
    """
    global boardx, boardy, shownBoard, hiddenBoard
    change = True
    while change == True:
        change = False
        for x in range(0,boardx):
            for y in range(0,boardy):
                if shownBoard[x][y] == 9:
                    # WEST
                    if x>0 and shownBoard[x-1][y] != hiddenBoard[x-1][y] and hiddenBoard[x-1][y] != 0:
                        change, shownBoard[x-1][y] = True, hiddenBoard[x-1][y]
                        buttonList[x-1][y] = tk.Label(master, image=Sweep.imgArr[int(shownBoard[x-1][y])])
                        buttonList[x-1][y].place(x=x*100-100, y=y*100)
                    # EAST
                    if x<boardx-1 and shownBoard[x+1][y] != hiddenBoard[x+1][y] and hiddenBoard[x+1][y] != 0:
                        change, shownBoard[x+1][y] = True, hiddenBoard[x+1][y]
                        buttonList[x+1][y] = tk.Label(master, image=Sweep.imgArr[int(shownBoard[x+1][y])])
                        buttonList[x+1][y].place(x=x*100+100, y=y*100)
                    # NORTH
                    if y>0 and shownBoard[x][y-1] != hiddenBoard[x][y-1] and hiddenBoard[x][y-1] != 0:
                        change, shownBoard[x][y-1] = True, hiddenBoard[x][y-1]
                        buttonList[x][y-1] = tk.Label(master, image=Sweep.imgArr[int(shownBoard[x][y-1])])
                        buttonList[x][y-1].place(x=x*100, y=y*100-100)
                    # SOUTH
                    if y<boardy-1 and shownBoard[x][y+1] != hiddenBoard[x][y+1] and hiddenBoard[x][y+1] != 0:
                        change, shownBoard[x][y+1] = True, hiddenBoard[x][y+1]
                        buttonList[x][y+1] = tk.Label(master, image=Sweep.imgArr[int(shownBoard[x][y+1])])
                        buttonList[x][y+1].place(x=x*100, y=y*100+100)