# this is the main .py file for the chessGame, that'll control all the other classes/modules

#window setup
from tkinter import *  #import tkinter
window: Tk = Tk()  # create the main window

#Chess game setup
from ChessBoardManager import *  #first we import the ChessBoardMangaer.py, which is used to manage the whole chess game
chessBoardManager = ChessBoard(window, 60)  #create a new ChessBoard class, which itself sets up everything else to start a chess game

window.mainloop()
