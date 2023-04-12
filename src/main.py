# this is the main .py file for the chessGame, that'll control all the other classes/modules

#window setup
from tkinter import *; #import tkinter

window: Tk = Tk(); # create the main window

#Chess game setup
from ChessBoardManager import *;
chessBoardManager = ChessBoard(window, 60);
chessBoardManager.createBoard();


window.mainloop();