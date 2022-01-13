###MineSweeper Game
##TODO:
"add leaderboard"
"add timer"
#Modules
import tkinter as tk
import random
import time
import Subroutines as sub

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
btnEasy = tk.Button(menu, text="Easy", image=imgArr[18], highlightthickness = 0, width = 350, height = 50, bd = 0, command=lambda: sub.gameSetup("easy"))
btnEasy.place(x=25, y=100)
btnNormal = tk.Button(menu, text="Normal", image=imgArr[19], highlightthickness = 0, width = 350, height = 50, bd = 0, command=lambda:sub.gameSetup("normal"))
btnNormal.place(x=25,y=175)
btnHard = tk.Button(menu, text="Hard", image=imgArr[20], highlightthickness = 0, width = 350, height = 50, bd = 0, command=lambda:sub.gameSetup("hard"))
btnHard.place(x=25,y=250)
btnLeader = tk.Button(menu, text="LeaderBoard", image=imgArr[21], highlightthickness = 0, width = 350, height = 50, bd = 0, command=lambda:sub.leaderboard())
btnLeader.place(x=25,y=325)
btnTutorial = tk.Button(menu, text="How to Play", image=imgArr[22], highlightthickness = 0, width = 350, height = 50, bd = 0, command=lambda:sub.tutorial())
btnTutorial.place(x=25,y=400)
