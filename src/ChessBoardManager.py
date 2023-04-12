

class ChessBoard:
    #consts
    ROWS: int = 8; #amount of rows on the chessBoard
    COLUMNS: int = 8; #amount of columns on the chessBoard
    
    def __init__(self, CELLSIZE: int) -> None:
        #from def
        #consts
        self.CELLSIZE = CELLSIZE;
        
        #board Parts
        self.fieldHandler: FieldHandler = FieldHandler(); #class that handles all the fields on the chessBoard
        
        pass
    
    def createBoard(self): #method that creates a canvas on the self.window, that'll contain the chessBoard
        
        #cycle through the whole board and add the field backgrounds
        
        pass;
    
    

class FieldHandler: #class that handles all the fields of a chess board
    #consts
    COLORS: tuple = ("white", "black") #colors used for the fields on the board
    
    def __init__(self) -> None:
        pass
    
    def createBoardFields(self, chessBoard: ChessBoard): #method that'll create the fields for a chessBoard on given chessBoard
        #TODO fieldCreation logic
        pass