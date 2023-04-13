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
        moves.extend(getLineMoves(chessBoard, copy.copy(self.pos), 1, 0))
        moves.extend(getLineMoves(chessBoard, copy.copy(self.pos), -1, 0))
        moves.extend(getLineMoves(chessBoard, copy.copy(self.pos), 0, 1))
        moves.extend(getLineMoves(chessBoard, copy.copy(self.pos), 0, -1))
        
        return moves; #return the calculated moves
    
    
    
class Bishop(ChessPiece):
    def __init__(self, pos: ChessBoardManager.BoardPos, color: Color) -> None:
        super().__init__(pos, color, "bishop");
        
    def getMoves(self, chessBoard: ChessBoardManager.ChessBoard) -> list:
        
        moves: list = []; #this list will contain all posibble moves and'll later be returned
            
        #get the line moves for each diagonal the bishop moves on
        moves.extend(getLineMoves(chessBoard, copy.copy(self.pos), 1, 1))
        moves.extend(getLineMoves(chessBoard, copy.copy(self.pos), -1, -1))
        moves.extend(getLineMoves(chessBoard, copy.copy(self.pos), -1, 1))
        moves.extend(getLineMoves(chessBoard, copy.copy(self.pos), 1, -1))
        
        return moves; #return the calculated moves
    
    

class Queen(ChessPiece):
    def __init__(self, pos: ChessBoardManager.BoardPos, color: Color) -> None:
        super().__init__(pos, color, "queen");
        
    def getMoves(self, chessBoard: ChessBoardManager.ChessBoard) -> list:
        
        moves: list = []; #this list will contain all posibble moves and'll later be returned
            
        #get the line moves for each row and column the queen moves on
        moves.extend(getLineMoves(chessBoard, copy.copy(self.pos), 1, 0))
        moves.extend(getLineMoves(chessBoard, copy.copy(self.pos), -1, 0))
        moves.extend(getLineMoves(chessBoard, copy.copy(self.pos), 0, 1))
        moves.extend(getLineMoves(chessBoard, copy.copy(self.pos), 0, -1))
        
        #get the line moves for each diagonal the queen moves on
        moves.extend(getLineMoves(chessBoard, copy.copy(self.pos), 1, 1))
        moves.extend(getLineMoves(chessBoard, copy.copy(self.pos), -1, -1))
        moves.extend(getLineMoves(chessBoard, copy.copy(self.pos), -1, 1))
        moves.extend(getLineMoves(chessBoard, copy.copy(self.pos), 1, -1))
        
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
def getLineMoves(chessBoard: ChessBoardManager.ChessBoard, pos: ChessBoardManager.BoardPos, xIncr: int, yIncr: int) -> list: #method that'll return all the moves on a line with given gradient, in a list
    
    moves = []; #list that'll be returned and contains all the possible moves on the line with given gradient
    startPos = copy.copy(pos); #get a copy of the given position to store the startPos, which is needed to create Move classes, as we need the piece at the start position for that
    
    
    #increase the values so the startPos is not on the moves list
    pos.x += xIncr;
    pos.y += yIncr;
    
    #check foreach pos on line if valid and if so add it to the moves list
    while (pos.x < ChessBoardManager.ChessBoard.COLUMNS and pos.x >= 0 and pos.y >= 0 and pos.y < ChessBoardManager.ChessBoard.ROWS): #check if the pos currently check for validation is even on the chessBoard
        moves.append(Move(chessBoard.getPieceAtPos(startPos), copy.copy(pos), Move.MoveType.NORMAL)); #add a copy of the pos to the move, a reference would be modified throughout the for loop, add the move to the later returned moves list, the move type is normal, as this is just a normal line move
        
        pos.x += xIncr;
        pos.y += yIncr;
        
        
    return moves; #finally return the moves list


class Move: #class that stores move endPos and moveType aswell as the piece to move, the move Type is quite important for performing moves like en passant and castling
    
    class MoveType(Enum): #enum that represents the MoveType of the chessPiece
        NORMAL = 0; #by normal chess move that does not fall into the following categories
        DOUBLEPAWN = 1; #move performed when a pawn moves 2 squares, this is needed for calculating en passant moves
        EN_PASSANT = 2; #google en passant, needed to perform a given en passant move properly
        CASTLING = 3; #any castling move, needed to perform a given castling move properly
    
    
    def __init__(self, piece: ChessPiece, moveTo: ChessBoardManager.BoardPos, moveType: int) -> None:
        
        self.pieceToMove = piece; #the piece that'll be moved, when this move was performed
        self.moveTo = moveTo; #the position the given piece moves to
        self.moveType = self.MoveType(moveType); #the type of move


def performMove(chessBoard: ChessBoardManager.ChessBoard, move: Move): #method that'll perform given move
    
    if move.moveType == Move.MoveType.NORMAL: #if it is normal move, we'll just move the piece to the moveTo position
        move.pieceToMove.pos = move.moveTo;
