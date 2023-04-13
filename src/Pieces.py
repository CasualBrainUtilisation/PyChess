#class that'll handle everything related to chess pieces

from enum import Enum; #so we can use Enums, used for piece color
import ChessBoardManager; #import the ChessBoardManager class, so we have acces to BoardPos ect.
import copy; #needed to copy the boardPos class when calculating moves

class Color(Enum): #enum used to store a piece's color
        White = 0;
        Black = 1;
    
    
class ChessPiece:
    
    def __init__(self, pos: ChessBoardManager.BoardPos, color: int, name: str) -> None:
        
        self.pos = pos; #this stores the piece position on the chessBoard
        self.color: Color = Color(color); #set the color of the piece
        
        self.name = name;
        

class Rook(ChessPiece):
    def __init__(self, pos: ChessBoardManager.BoardPos, color: Color) -> None:
        super().__init__(pos, color, "rook");
        
    def getMoves(self, chessBoard: ChessBoardManager.ChessBoard) -> list:
        
        moves: list = []; #this list will contain all posibble moves and'll later be returned
            
        #get the line moves for each row and column the rook moves on
        moves.extend(getLineMoves(copy.copy(self.pos), 1, 0))
        moves.extend(getLineMoves(copy.copy(self.pos), -1, 0))
        moves.extend(getLineMoves(copy.copy(self.pos), 0, 1))
        moves.extend(getLineMoves(copy.copy(self.pos), 0, -1))
        
        return moves; #return the calculated moves
    
    
    
class Bishop(ChessPiece):
    def __init__(self, pos: ChessBoardManager.BoardPos, color: Color) -> None:
        super().__init__(pos, color, "bishop");
        
    def getMoves(self, chessBoard: ChessBoardManager.ChessBoard) -> list:
        
        moves: list = []; #this list will contain all posibble moves and'll later be returned
            
        #get the line moves for each diagonal the bishop moves on
        moves.extend(getLineMoves(copy.copy(self.pos), 1, 1))
        moves.extend(getLineMoves(copy.copy(self.pos), -1, -1))
        moves.extend(getLineMoves(copy.copy(self.pos), -1, 1))
        moves.extend(getLineMoves(copy.copy(self.pos), 1, -1))
        
        return moves; #return the calculated moves
    
    

class Queen(ChessPiece):
    def __init__(self, pos: ChessBoardManager.BoardPos, color: Color) -> None:
        super().__init__(pos, color, "queen");
        
    def getMoves(self, chessBoard: ChessBoardManager.ChessBoard) -> list:
        
        moves: list = []; #this list will contain all posibble moves and'll later be returned
            
        #get the line moves for each row and column the queen moves on
        moves.extend(getLineMoves(copy.copy(self.pos), 1, 0))
        moves.extend(getLineMoves(copy.copy(self.pos), -1, 0))
        moves.extend(getLineMoves(copy.copy(self.pos), 0, 1))
        moves.extend(getLineMoves(copy.copy(self.pos), 0, -1))
        
        #get the line moves for each diagonal the queen moves on
        moves.extend(getLineMoves(copy.copy(self.pos), 1, 1))
        moves.extend(getLineMoves(copy.copy(self.pos), -1, -1))
        moves.extend(getLineMoves(copy.copy(self.pos), -1, 1))
        moves.extend(getLineMoves(copy.copy(self.pos), 1, -1))
        
        return moves; #return the calculated moves
    
    
    
class Pawn(ChessPiece):
    def __init__(self, pos: ChessBoardManager.BoardPos, color: Color) -> None:
        super().__init__(pos, color, "pawn");
        
    def getMoves(self, chessBoard: ChessBoardManager.ChessBoard) -> list:
        #TODO logic to get moves
        return [self.pos];
    
    
    
class King(ChessPiece):
    def __init__(self, pos: ChessBoardManager.BoardPos, color: Color) -> None:
        super().__init__(pos, color, "king");
        
    def getMoves(self, chessBoard: ChessBoardManager.ChessBoard) -> list:
        #TODO logic to get moves
        return [self.pos];
    
    
    
class Knight(ChessPiece):
    def __init__(self, pos: ChessBoardManager.BoardPos, color: Color) -> None:
        super().__init__(pos, color, "knight");
        
    def getMoves(self, chessBoard: ChessBoardManager.ChessBoard) -> list:
        #TODO logic to get moves
        return [self.pos];




#getting moves
def getLineMoves(pos: ChessBoardManager.BoardPos, xIncr: int, yIncr: int) -> list: #method that'll return all the moves on a line with given gradient, in a list
    
    moves = []; #list that'll be returned and contains all the possible moves on the line with given gradient
    
    #increase the values so the startPos is not on the moves list
    pos.x += xIncr;
    pos.y += yIncr;
    
    #check foreach pos on line if valid and if so add it to the moves list
    while (pos.x < ChessBoardManager.ChessBoard.COLUMNS and pos.x >= 0 and pos.y >= 0 and pos.y < ChessBoardManager.ChessBoard.ROWS): #check if the pos currently check for validation is even on the chessBoard
        moves.append(copy.copy(pos)); #add a copy of the pos to the moves list, a reference would be modified throughout the for loop
        
        pos.x += xIncr;
        pos.y += yIncr;
        
        
    return moves; #finally return the moves list


class Move: #class that stores move endPos and moveType, the move Type is quite important for performing moves like en passant and castling
    pass;