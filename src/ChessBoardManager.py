from tkinter import *; #import the tkinter module
import FEN; #needed to load pieces from FEN

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
        self.__fieldHandler: FieldHandler = FieldHandler(self); #class that handles all the fields on the chessBoard
        self.__pieceVisualisation: PieceVisualisation = PieceVisualisation(self); #class that handles the visual representation of the current pieces
        
        #pieces
        self.pieces = FEN.LoadPositionFromFEN("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"); #self.pieces represents the pieces currently on the board (they store their pos theirself), here we set it to the normal start posiiton
    
    def createBoard(self): #method that creates a canvas on the self.window, that'll contain the chessBoard
        
        self.canvas = Canvas(self.WINDOW, width = self.CELLSIZE * ChessBoard.COLUMNS, height = self.CELLSIZE * ChessBoard.ROWS) #setup a canvas where field, pieces  ect. can be placed on
        self.canvas.pack(); # add the canvas to the window
        
        self.canvas.bind("<Button-1>", self.boardClicked); #add the boardClicked event listener, so something happens if the user clicks on the chessBoard
        
        
        #call methods of the classes handling things like fields and pieces, to set them up
        self.__fieldHandler.createBoardFields(); #creates the fields for the chessBoard
        self.__pieceVisualisation.createImages(); #creates the images, which will show the pieces, for first those will be blank
    
    def boardClicked(self, event): #mehtod that'll be called every time the user clicks on a field on the chessBoard
        
        #calculate the field the user clicked on
        print(str(event.x // self.CELLSIZE) + "|" + str(event.y // self.CELLSIZE));
        
    
    

class FieldHandler: #class that handles all the fields of a chess board
    #consts
    COLORS: tuple = ("white", "black") #colors used for the fields on the board
    
    def __init__(self, chessBoard: ChessBoard) -> None:
        #from def
        self.__chessBoard = chessBoard;
        
        pass;
    
    def createBoardFields(self): #method that'll create the fields for the self.chessBoard
        
        #cycle through the whole board and add the field backgrounds
        for row in range(ChessBoard.ROWS):
            for column in range(ChessBoard.COLUMNS):
                self.__chessBoard.canvas.create_rectangle(self.__chessBoard.CELLSIZE * column, self.__chessBoard.CELLSIZE * row, self.__chessBoard.CELLSIZE * (column + 1), self.__chessBoard.CELLSIZE * (row + 1), fill = FieldHandler.COLORS[(row+column) % 2]); #create a rectangle add the current position, with the correct field color, on the chessBoard's canvas
                

class PieceVisualisation: #class that will handle the images, showing the chessPieces on the board
    def __init__(self, chessBoard: ChessBoard) -> None:
        
        #from def
        self.__chessBoard = chessBoard;
        
    def createImages(self): #method, that adds a blank image on each chessBoard Field, that later'll show an image of a piece, if the field contains one
        
        self.pieceImages = []; #this variable will store all the created piece Images, which later'll be used to show the pieces on the board
        
        #cycle through the whole board and add the blank images to the canvas
        for row in range(ChessBoard.ROWS):
            
            self.pieceImages.append([]); #add a row to the self.pieceImages
            
            for column in range(ChessBoard.COLUMNS):
                
                pieceImage = PhotoImage();
                self.__chessBoard.canvas.create_image(self.__chessBoard.CELLSIZE * column, self.__chessBoard.CELLSIZE * row, anchor = "nw", image = pieceImage);
                
    
                


class BoardPos: #class that stores a position on the chessBoard
    def __init__(self, x: int, y: int) -> None: 
        
        self.x = x;
        self.y = y;
        
       
    
def IsPosValid(pos: BoardPos) -> bool: #returns false if the given position is not on the board, else returns true
    if (pos.x < 0 or pos.x >= ChessBoard.COLUMNS or pos.y < 0 or pos.y >= ChessBoard.ROWS):
        return False;
    return True;
                
                