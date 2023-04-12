#module that'll be able to load FENs
from ChessBoardManager import *; #needed to use BoardPos
from Pieces import *; #needed to return lists of pieces when loadin an FEN


def LoadPositionFromFEN(FEN: str) -> list: #method that'll return a list of pieces, which can build a posiition loaded from given FEN on the chessBoard, it'll return None if the FEN is invalid
    row: int = 0; #the row currently generating
    column: int = 0; #the column currently generating
    index: int = 0; #the index in the FEN string, currently add

    curChar: str; #the character of the FEN string, currently read
    
    pieces: list = []; #the list of pieces loaded by the FEN, that'll be returned later


    if len(FEN) == 0: #if the FEN string is empty return NONE
        return None;
    
    while FEN[index].isspace(): #if the current character is a white space, repeat until it's not
        index += 1; #increase the index, to get the first none space
        
        if len(FEN) == index: #return None, if we have checked the whole FEN string
            return None;
    
    while FEN[index].isspace() == False: #load the position from the FEN, character for character, repeat until the current character is blank
        curChar = FEN[index]; #set the currently checked character
        
        if (curChar.isalpha()): #if the currently checked character is only made of letters continue here
            
            if (BoardPos(column,row) == False): #if the currently checked position is not valid, but there is a letter there, the FEN is invalid, so we'll return null
                return None;
            
            pos: BoardPos = BoardPos(column, row); #get the currently checked position
            
            if curChar.lower() == "r": #check if the currenlty checked charater is a rook
                pieces.append(Rook(pos, curChar.islower())) #add a rook at the currenlty checked position
                
            elif curChar.lower() == "b": #check if the currenlty checked charater is a bishop
                pieces.append(Bishop(pos, curChar.islower())) #add a bishop at the currenlty checked position
                
            elif curChar.lower() == "q": #check if the currenlty checked charater is a Queen
                pieces.append(Queen(pos, curChar.islower())) #add a Queen at the currenlty checked position
                
            elif curChar.lower() == "k": #check if the currenlty checked charater is a King
                pieces.append(King(pos, curChar.islower())) #add a King at the currenlty checked position
                
            elif curChar.lower() == "p": #check if the currenlty checked charater is a Pawn
                pieces.append(Pawn(pos, curChar.islower())) #add a Pawn at the currenlty checked position
                
            elif curChar.lower() == "b": #check if the currenlty checked charater is a Knight
                pieces.append(Knight(pos, curChar.islower())) #add a Knight at the currenlty checked position
                
            else:
                return None; #the character wasn't valid, so the FEN is invalid, we'll return None
        
        elif curChar.isnumeric(): #if the currenctly checked character is a number, we'll add that to the currently checked column (that's how FENs work)
            column += int(curChar);
                
        elif curChar == "/": #if the currently checked character is a '/', we'll set the currently checked column to 0 and increase the currently checked row by 1
            column = 0;
            row += 1;
            
        if (row > ChessBoard.ROWS or column > ChessBoard.COLUMNS): #row or column values equal ROWS or COLUMNS are normal as the '/' comes directly after them, if they are bigger though, the FEN is invalid, return None
            return None;

        index += 1; #increase the index, so we'll check the next character
        
        if len(FEN) == index: #if we have checked the whole FEN string break out of the while loop and return the pieces
            break;


    return pieces;