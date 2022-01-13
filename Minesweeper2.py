###MineSweeper Game
##TODO:
"add leaderboard"
"add timer"
#Modules
import tkinter as tk
import random
import time

def interact(tilex,tiley):
    global selectionMode, gameRun
    if gameRun == True:
        if tilex < boardx and tiley < boardy and tilex > -1 and tiley > -1:
            if selectionMode == "dig":
                dig(tilex,tiley)
            elif selectionMode == "flag":
                flag(tilex,tiley)
            elif selectionMode == "hint":
                hint(tilex,tiley)

def changeMode(mode):
    global selectionMode
    selectionMode = mode

def gameSetup(difficulty): ## TODO Replace gameSetup() with GUI inputs
    global numberOfMines, boardx, boardy, gameRun, master
    isFirstMove = True
    gameRun = True
    if difficulty == "easy":
        boardx, boardy, numberOfMines = 20, 10, 25
    if difficulty == "normal":
        boardx, boardy, numberOfMines= 20, 10, 40
    if difficulty == "hard":
        boardx, boardy, numberOfMines= 20, 10, 50
    if difficulty == "custom":
        boardx, boardy, = 10, 5
        numberOfMines = int(input("number of mines: "))
    master = tk.Toplevel()
    master.title("Minesweeper")
    master.geometry("1000x600")
    shovelBtn = tk.Button(master, image = imgArr[11],
                          command=lambda: changeMode("dig"),
                          highlightthickness = 0, bd = 0
                          )
    shovelBtn.place(x=450, y=500)
    flagBtn = tk.Button(master, image = imgArr[10],
                        command=lambda: changeMode("flag"),
                        highlightcolor = "blue",
                        highlightthickness = 0, bd = 0
                        )
    flagBtn.place(x=500,y=500)
    boardGen()
    hintBtn = tk.Button(master, image = imgArr[17],
                        command=lambda: changeMode("hint"),
                        highlightthickness = 0, bd = 0
                        )
    hintBtn.place(x=560, y=500)

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

            buttonList[x][y] = tk.Button(master, image=imgArr[int(shownBoard[x][y])],
                                             command=lambda x=x, y=y: interact(x,y),
                                             bg="#f3f3f3", fg="#ffffff",
                                             relief = "groove",
                                             highlightthickness = 0, bd = 0,
                                             activebackground='#999999')
            buttonList[x][y].place(x=x*50,y=y*50)

def boardGen():
    """
    Generates a shownBoard and buttonList, for the player to see and interact with.
    Generates a hiddenBoard, for the system to compare values
    and to copy across to the shownBoard when necessary.
    """
    global boardx, boardy, isFirstMove, hiddenBoard, shownBoard, buttonList
    hiddenBoard = [[9 for y in range(0,boardy)] for x in range(0,boardx)]
    shownBoard = [[15 for y in range(0,boardy)] for x in range(0,boardx)]
    buttonList = [[None for y in range(0,boardy)] for x in range(0,boardx)]
    isFirstMove = True
    for x in range(0,boardx):
            for y in range(0,boardy):
                buttonList[x][y] = tk.Button(master, image=imgArr[int(shownBoard[x][y])],
                                             command=lambda x=x, y=y: interact(x,y),
                                             bg="#f3f3f3", fg="#ffffff",
                                             highlightthickness = 0, bd = 0,
                                             activebackground='#999999')
                buttonList[x][y].place(x=x*50,y=y*50)

def dig(tilex,tiley):
    """
    Reveals the contents of the selected tile.
    If the tile is a mine, then the game is over and the player loses.
    """
    global isFirstMove, hiddenBoard, shownBoard, boardx, boardy, buttonList, numberOfMines, startTime
    if isFirstMove == True:
        remainingMines = numberOfMines
        randomx, randomy = int(tilex), int(tiley)

        """
        Deploys all mines on the board
        """
        while remainingMines > 0:
            if hiddenBoard[randomx][randomy] == 9 and (randomx < int(tilex-1) or randomy < int(tiley-1) or randomx > int(tilex+1) or randomy > int(tiley+1)):
                remainingMines -= 1
                hiddenBoard[randomx][randomy] = 0
            randomx, randomy, = random.randint(0,boardx-1), random.randint(0,boardy-1)
        number()
        buttonList = [[None for y in range(0,boardy)] for x in range(0,boardx)]
        for x in range(boardx):
            for y in range(boardy):
                buttonList[x][y] = tk.Button(master, image=imgArr[int(shownBoard[x][y])],
                                             command=lambda x=x, y=y: interact(x,y),
                                             bg="#f3f3f3", fg="#ffffff",
                                             relief = "groove",
                                             highlightthickness = 0, bd = 0,
                                             activebackground='#999999')
                buttonList[x][y].place(x=x*50,y=y*50)
        startTime = time.perf_counter()
        isFirstMove = False
    shownBoard[int(tilex)][int(tiley)] = hiddenBoard[int(tilex)][int(tiley)] # displays the hidden value on the board
    buttonList[tilex][tiley] = tk.Label(master, highlightthickness = 0, bd = 0, image=imgArr[int(shownBoard[tilex][tiley])])
    buttonList[tilex][tiley].place(x=tilex*50, y=tiley*50)
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
        shownBoard[tilex][tiley] = 15  ## ADD RESOURCE ##
    else:
        shownBoard[tilex][tiley] = 10
    buttonList[tilex][tiley] = tk.Button(master, image=imgArr[int(shownBoard[tilex][tiley])], highlightthickness = 0, bd = 0, command=lambda x=tilex, y=tiley:interact(x,y))
    buttonList[tilex][tiley].place(x=tilex*50, y=tiley*50)

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
                        buttonList[x-1][y] = tk.Label(master, highlightthickness = 0, bd = 0, image=imgArr[int(shownBoard[x-1][y])])
                        buttonList[x-1][y].place(x=x*50-50, y=y*50)
                    # EAST
                    if x<boardx-1 and shownBoard[x+1][y] != hiddenBoard[x+1][y] and hiddenBoard[x+1][y] != 0:
                        change, shownBoard[x+1][y] = True, hiddenBoard[x+1][y]
                        buttonList[x+1][y] = tk.Label(master, highlightthickness = 0, bd = 0, image=imgArr[int(shownBoard[x+1][y])])
                        buttonList[x+1][y].place(x=x*50+50, y=y*50)
                    # NORTH
                    if y>0 and shownBoard[x][y-1] != hiddenBoard[x][y-1] and hiddenBoard[x][y-1] != 0:
                        change, shownBoard[x][y-1] = True, hiddenBoard[x][y-1]
                        buttonList[x][y-1] = tk.Label(master, highlightthickness = 0, bd = 0, image=imgArr[int(shownBoard[x][y-1])])
                        buttonList[x][y-1].place(x=x*50, y=y*50-50)
                    # SOUTH
                    if y<boardy-1 and shownBoard[x][y+1] != hiddenBoard[x][y+1] and hiddenBoard[x][y+1] != 0:
                        change, shownBoard[x][y+1] = True, hiddenBoard[x][y+1]
                        buttonList[x][y+1] = tk.Label(master, highlightthickness = 0, bd = 0, image=imgArr[int(shownBoard[x][y+1])])
                        buttonList[x][y+1].place(x=x*50, y=y*50+50)
                    # NORTHWEST
                    if y>0 and x>0 and shownBoard[x-1][y-1] != hiddenBoard[x-1][y-1] and hiddenBoard[x-1][y-1] != 0:
                        change, shownBoard[x-1][y-1] = True, hiddenBoard[x-1][y-1]
                        buttonList[x-1][y-1] = tk.Label(master, highlightthickness = 0, bd = 0, image=imgArr[int(shownBoard[x-1][y-1])])
                        buttonList[x-1][y-1].place(x=x*50-50, y=y*50-50)
                    # NORTHEAST
                    if y>0 and x<boardx-1 and shownBoard[x+1][y-1] != hiddenBoard[x+1][y-1] and hiddenBoard[x+1][y-1] != 0:
                        change, shownBoard[x+1][y-1] = True, hiddenBoard[x+1][y-1]
                        buttonList[x+1][y-1] = tk.Label(master, highlightthickness = 0, bd = 0, image=imgArr[int(shownBoard[x+1][y-1])])
                        buttonList[x+1][y-1].place(x=x*50+50, y=y*50-50)
                    # SOUTHWEST
                    if y<boardy-1 and x>0 and shownBoard[x-1][y+1] != hiddenBoard[x-1][y+1] and hiddenBoard[x-1][y+1] != 0:
                        change, shownBoard[x-1][y+1] = True, hiddenBoard[x-1][y+1]
                        buttonList[x-1][y+1] = tk.Label(master, highlightthickness = 0, bd = 0, image=imgArr[int(shownBoard[x-1][y+1])])
                        buttonList[x-1][y+1].place(x=x*50-50, y=y*50+50)
                    # SOUTHEAST
                    if y<boardy-1 and x<boardx-1 and shownBoard[x+1][y+1] != hiddenBoard[x+1][y+1] and hiddenBoard[x+1][y+1] != 0:
                        change, shownBoard[x+1][y+1] = True, hiddenBoard[x+1][y+1]
                        buttonList[x+1][y+1] = tk.Label(master, highlightthickness = 0, bd = 0, image=imgArr[int(shownBoard[x+1][y+1])])
                        buttonList[x+1][y+1].place(x=x*50+50, y=y*50+50)

def gameOver():
    global shownBoard, hiddenBoard, gameRun, startTime, boardx, boardy
    gameRun = False
    endTime = time.perf_counter()
    timeTaken = endTime - startTime
    print(timeTaken)
    for x in range(boardx):
        for y in range(boardy):
            shownBoard[x][y] = hiddenBoard[x][y]
            if shownBoard[x][y] == 0:
                buttonList[x][y] = tk.Label(master, highlightthickness = 0, bd = 0, image=imgArr[16])
                buttonList[x][y].place(x=x*50,y=y*50)
                
def hint(tilex,tiley):
    global hints, shownBoard, hiddenBoard
    if hints > 0:
        shownBoard[tilex][tiley] = hiddenBoard[tilex][tiley]
        buttonList[tilex][tiley] = tk.Label(master, highlightthickness = 0, bd = 0, image=imgArr[int(shownBoard[tilex][tiley])])
        buttonList[tilex][tiley].place(x=tilex*50,y=tiley*50)
        hints -= 1
    else:
        print("Error: not enough hints remaining.")
        
def leaderboard():
    lblLeaderboard.place(x=500,y=30)
    lblTutorial.place_forget()

def leaderboardGenerate():
    global leaderboard
    

def tutorial():
    lblTutorial.place(x=405,y=15)
    lblLeaderboard.place_forget()

#Data Structures
hints = 3
randomx = 0
randomy = 0
numberOfMines = 0
boardx = 5
boardy = 5
shownBoard = []
hiddenBoard = []
buttonList = []
isFirstMove = False
gameRun = False
selectionMode = "dig"
leaderBoard = []
startTime = 0
endTime = 0

menu = tk.Tk()
menu.title("Minesweeper")
menu.geometry("1000x600")

#Resources
img1 = '1.png'
img2 = '2.png'
img3 = '3.png'
img4 = '4.png'
img5 = '5.png'
img6 = '6.png'
img7 = '7.png'
img8 = '8.png'
img_mine = 'mine.png'
img_flag = 'flag.png'
img_shovel = 'shovel.png'
img_restart = 'restart.png'
img_safe = 'safe.png'
img_game_over = 'gameOver.png'
img_menu = "menu.png"
img_grass = "grass.png"
img_boom = "boom.png"
img_hint = "hint.png"
img_easy = "easy.png"
img_normal = "normal.png"
img_hard = "hard.png"
img_leader = "leader.png"
img_howtoplay = "howtoplay.png"
img_tutorial_text = "tutorial_text.png"
imgArr = [tk.PhotoImage(file=img_mine), # 0
          tk.PhotoImage(file=img1), # 1
          tk.PhotoImage(file=img2), # 2
          tk.PhotoImage(file=img3), # 3
          tk.PhotoImage(file=img4), # 4
          tk.PhotoImage(file=img5), # 5
          tk.PhotoImage(file=img6), # 6
          tk.PhotoImage(file=img7), # 7
          tk.PhotoImage(file=img8), # 8
          tk.PhotoImage(file=img_safe), # 9
          tk.PhotoImage(file=img_flag), # 10
          tk.PhotoImage(file=img_shovel), # 11
          tk.PhotoImage(file=img_restart), # 12
          tk.PhotoImage(file=img_menu), # 13
          tk.PhotoImage(file=img_game_over), # 14
          tk.PhotoImage(file=img_grass), # 15
          tk.PhotoImage(file=img_boom), # 16
          tk.PhotoImage(file=img_hint), # 17
          tk.PhotoImage(file=img_easy), # 18
          tk.PhotoImage(file=img_normal), # 19
          tk.PhotoImage(file=img_hard), # 20
          tk.PhotoImage(file=img_leader), # 21
          tk.PhotoImage(file=img_howtoplay), # 22
          tk.PhotoImage(file=img_tutorial_text) # 23
          ]
leaderText = ""
lblTitle = tk.Label(menu, image = imgArr[13])
lblTitle.pack()
lblTutorial = tk.Label(menu, image = imgArr[23], width = 571, height = 565, bd = 0)
lblLeaderboard = tk.Label(menu, bd=0, text=leaderText)
btnEasy = tk.Button(menu, text="Easy", image=imgArr[18], highlightthickness = 0, width = 350, height = 50, bd = 0, command=lambda: gameSetup("easy"))
btnEasy.place(x=25, y=100)
btnNormal = tk.Button(menu, text="Normal", image=imgArr[19], highlightthickness = 0, width = 350, height = 50, bd = 0, command=lambda:gameSetup("normal"))
btnNormal.place(x=25,y=175)
btnHard = tk.Button(menu, text="Hard", image=imgArr[20], highlightthickness = 0, width = 350, height = 50, bd = 0, command=lambda:gameSetup("hard"))
btnHard.place(x=25,y=250)
btnLeader = tk.Button(menu, text="LeaderBoard", image=imgArr[21], highlightthickness = 0, width = 350, height = 50, bd = 0, command=lambda:leaderboard())
btnLeader.place(x=25,y=325)
btnTutorial = tk.Button(menu, text="How to Play", image=imgArr[22], highlightthickness = 0, width = 350, height = 50, bd = 0, command=lambda:tutorial())
btnTutorial.place(x=25,y=400)

tk.mainloop()
