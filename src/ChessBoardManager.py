from tkinter import *; #import the tkinter module

class ChessBoard:
    #consts
    ROWS: int = 8; #amount of rows on the chessBoard
    COLUMNS: int = 8; #amount of columns on the chessBoard
    
    def __init__(self, WINDOW: Tk, CELLSIZE: int) -> None:
        #from def
        #consts
        self.WINDOW = WINDOW;
        self.CELLSIZE = CELLSIZE;
        
        #board Parts
        self.fieldHandler: FieldHandler = FieldHandler(); #class that handles all the fields on the chessBoard
        
        pass
    
    def createBoard(self): #method that creates a canvas on the self.window, that'll contain the chessBoard
        
        self.canvas = Canvas(self.WINDOW, width = self.CELLSIZE * ChessBoard.COLUMNS, height = self.CELLSIZE * ChessBoard.ROWS) #setup a canvas where field, pieces  ect. can be placed on
        self.canvas.pack(); # add the canvas to the window
        
        self.canvas.bind("<Button-1>", self.boardClicked); #add the boardClicked event listener, so something happens if the user clicks on the chessBoard
        
        
        #call methods of the classes handling things like fields and pieces, to set them up
        self.fieldHandler.createBoardFields(self); #creates the fields for the chessBoard
        
        pass;
    
    def boardClicked(self, event): #mehtod that'll be called every time the user clicks on a field on the chessBoard
        print("u clicked a field");
        
    
    

class FieldHandler: #class that handles all the fields of a chess board
    #consts
    COLORS: tuple = ("white", "black") #colors used for the fields on the board
    
    def __init__(self) -> None:
        pass
    
    def createBoardFields(self, chessBoard: ChessBoard): #method that'll create the fields for a chessBoard on given chessBoard
        
        #cycle through the whole board and add the field backgrounds
        for row in range(ChessBoard.ROWS):
            for column in range(ChessBoard.COLUMNS):
                chessBoard.canvas.create_rectangle(chessBoard.CELLSIZE * column, chessBoard.CELLSIZE * row, chessBoard.CELLSIZE * (column + 1), chessBoard.CELLSIZE * (row + 1), fill = FieldHandler.COLORS[(row+column) % 2]); #create a rectangle add the current position, with the correct field color, on the chessBoard's canvas
                
                