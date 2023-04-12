# this is the main .py file for the chessGame, that'll control all the other classes/modules

#window setup
from tkinter import *; #import tkinter

window: Tk = Tk(); # create the main window

#Chess game setup
from ChessBoardManager import *;
chessBoardManager = ChessBoard(window, 60);
chessBoardManager.createBoard();

import FEN;
print(FEN.LoadPositionFromFEN("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"));

window.mainloop();