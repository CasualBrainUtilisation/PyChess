from tkinter import *; #import the tkinter module
import FEN; #needed to load pieces from FEN
from PIL import Image, ImageTk; #this module is needed to resize images

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
        
        #setup the chessBoard Visuals
        self.createBoard();
        
        #pieces
        self.pieces = FEN.LoadPositionFromFEN("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"); #self.pieces represents the pieces currently on the board (they store their pos theirself), here we set it to the normal start posiiton
        self.__pieceVisualisation.updatePieceImages(); #update the piece images to show the just loaded start position
        
        
    def createBoard(self): #method that creates a canvas on the self.window, that'll contain the chessBoard
        
        self.canvas = Canvas(self.WINDOW, width = self.CELLSIZE * ChessBoard.COLUMNS, height = self.CELLSIZE * ChessBoard.ROWS) #setup a canvas where field, pieces  ect. can be placed on
        self.canvas.pack(); # add the canvas to the window
        
        self.canvas.bind("<Button-1>", self.boardClicked); #add the boardClicked event listener, so something happens if the user clicks on the chessBoard
        
        
        #call methods of the classes handling things like fields and pieces, to set them up
        self.__fieldHandler.createBoardFields(); #creates the fields for the chessBoard
        self.__pieceVisualisation.createImages(); #creates the images, which will show the pieces, for first those will be blank
    
    def boardClicked(self, event): #mehtod that'll be called every time the user clicks on a field on the chessBoard
        
        #calculate the field the user clicked on and store it in a BoardPos class
        pos: BoardPos = BoardPos(event.x // self.CELLSIZE, event.y // self.CELLSIZE)
        
        for piece in self.pieces:
            if (AreSamePos(pos, piece.pos)): #if the piece is placed on the field clicked on
                print(piece.getMoves(self)); #print the valid moves for the piece
        
    
    

class FieldHandler: #class that handles all the fields of a chess board
    #consts
    COLORS: tuple = ("white", "#1A1A1A") #colors used for the fields on the board, fields can not be pure black, as then they would hide the piece images
    
    def __init__(self, chessBoard: ChessBoard) -> None:
        #from def
        self.__chessBoard = chessBoard;
        
        pass;
    
    def createBoardFields(self) -> None: #method that'll create the fields for the self.chessBoard
        
        #cycle through the whole board and add the field backgrounds
        for row in range(ChessBoard.ROWS):
            for column in range(ChessBoard.COLUMNS):
                self.__chessBoard.canvas.create_rectangle(self.__chessBoard.CELLSIZE * column, self.__chessBoard.CELLSIZE * row, self.__chessBoard.CELLSIZE * (column + 1), self.__chessBoard.CELLSIZE * (row + 1), fill = FieldHandler.COLORS[(row+column) % 2]); #create a rectangle add the current position, with the correct field color, on the chessBoard's canvas
                

class PieceVisualisation: #class that will handle the images, showing the chessPieces on the board
    def __init__(self, chessBoard: ChessBoard) -> None:
        
        #from def
        self.__chessBoard = chessBoard;
        
    def createImages(self) -> None: #method, that adds a blank image on each chessBoard Field, that later'll show an image of a piece, if the field contains one

        self.pieceImages = [ [] for i in range(ChessBoard.ROWS)]; #this variable will store all the created piece Images, which later'll be used to show the pieces on the board
        
        #cycle through the whole board and add the blank images to the canvas
        for row in range(ChessBoard.ROWS):
            
            for column in range(ChessBoard.COLUMNS):
                
                pieceImage = PhotoImage(); #create a blank imgae
                
                canvasIMG = self.__chessBoard.canvas.create_image(self.__chessBoard.CELLSIZE * column, self.__chessBoard.CELLSIZE * row, anchor = "nw", image = pieceImage);
                self.pieceImages[row].append([canvasIMG, pieceImage]); #add the image to the board and referernce it in the  pieceImages list, also referenece the PhotoImage, to show the PhotoImage, you always have to keep a reference for some reason (took me a decade to figure out)
                
    def updatePieceImages(self) -> None: #method that'll update the pieceImages, to show the current chessBoard.pieces
        for piece in self.__chessBoard.pieces: #update the pieceImages prpoerly, for all the pieces in the chessBoard.pieces list
            
            img: Image = Image.open(PieceVisualisation.getPieceImage(piece)); #open the image with PIL.Image #TODO let this be the actual piece image
            print (img.mode);
            img = img.resize((self.__chessBoard.CELLSIZE, self.__chessBoard.CELLSIZE), Image.ANTIALIAS); #Resize the Image to CellSize * CellSize using PIL.Image.resize
            photoImg: PhotoImage = ImageTk.PhotoImage(img); #load the resized image as photoimage using PIL.ImageTk
            
            self.pieceImages[piece.pos.y][piece.pos.x][1] = photoImg; #update the reference to the PhotoImage(), you always have to keep a reference to the photoImage of a photo on canvas, else it won't show
            self.__chessBoard.canvas.itemconfig(self.pieceImages[piece.pos.y][piece.pos.x][0], image = photoImg); #set the actual image at the piece.pos to the new 1
       
       
    
    @staticmethod
    def getPieceImage(piece) -> str: #method used to get the image path for given chessPieceType
        import Pieces; #this method needs the pieces imported, to get their color and type
        
        FILE_EXT = ".png"; #the file extension for the piece images, shouhld be put into this variable
        START_PATH = "src\\images\\pieces\\"; #the start of the pieceImagePath, it leads to the dir all the piece images are stored in
        
        colorChar = str(piece.color.name)[0].lower(); #the character of the pieceImage that represents the piece color, 'w' for white, 'b' for black, this can be aquired by getting the first character of the piece.color.
        pieceChar = piece.name[0]; #the character representing the pieceType in the pieceImage name, this can be get by getting the first character of the piece.name.
        
        return START_PATH + colorChar + pieceChar + FILE_EXT; #return the full image path
            
            
                
    
                


class BoardPos: #class that stores a position on the chessBoard
    def __init__(self, x: int, y: int) -> None: 
        
        self.x = x;
        self.y = y;
        

def AreSamePos(pos1: BoardPos, pos2: BoardPos) -> bool: #method that checks if two BoardPos classes, store the same board position, if so returns true, else false
    
    if pos1.x == pos2.x and pos1.y == pos2.y: #if pos1 and pos2 are the same position return true
        return True;
    
    return False; #return false as pos1 and pos2 were not the same position
       
    
def IsPosValid(pos: BoardPos) -> bool: #returns false if the given position is not on the board, else returns true
    if (pos.x < 0 or pos.x >= ChessBoard.COLUMNS or pos.y < 0 or pos.y >= ChessBoard.ROWS):
        return False;
    return True;
                
                