###MineSweeper Game
##TODO:
"""
- Replace test() with GUI inputs
- Replace gamesetup() with GUI inputs
- ln 186 add blank resource
"""
#Modules
import tkinter as tk
import random
import time
import Subroutines as sub

#Data Structures
numberOfMines =0
boardx = 5
boardy = 5
shownBoard = []
hiddenBoard = []
isFirstMove = False
buttonList = []
randomx = 0
randomy = 0
selectionMode = "dig"

#Subroutines
def test(): ## TODO Replace test() with GUI inputs
    global selectionMode, shownBoard
    sub.gameSetup("easy") # asks for difficulty + sets boardx, boardy, numberOfMines
    sub.boardGen() # generates shownBoard and hiddenBoard

##def gameOver():
##    GO = tk.Toplevel()
##    GO.title("Game Over")
##    GO.geometry("1000x500")





gameRun = False
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
          tk.PhotoImage(file=img_menu)] # 13
lblTitle = tk.Label(menu, image = imgArr[13])
lblTitle.pack()
btnEasy = tk.Button(menu, text="Easy", command=lambda: sub.gameSetup("easy"))
btnEasy.place(x=100, y=100)
