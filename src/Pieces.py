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
        super().__init__(pos, color, "r");
        
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
        super().__init__(pos, color, "b");
        
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
        super().__init__(pos, color, "q");
        
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
        super().__init__(pos, color, "p");
        
    def getMoves(self, chessBoard: ChessBoardManager.ChessBoard) -> list:
        
        moves = []; #this list will later be returned and stores all the valid moves the piece has
        
        pawnDir = (-1,1) #the direction the pawn goes to (up/down), use the pieces color as index, to get the correct one for the related piece
        pawnStartPosY = (ChessBoardManager.ChessBoard.ROWS - 1 + pawnDir[0], 0 + pawnDir[1]) #the start position for pawn colors (white,black), again use self.color.value as index
        
        pieceInFront: ChessPiece = chessBoard.getPieceAtPos(ChessBoardManager.BoardPos(self.pos.x, self.pos.y + pawnDir[self.color.value])); #get the piece at the square in front of the pawn
        if pieceInFront is None: #if there is no piece at the position in front of the pawn, add it to the moves list
            moves.append(Move(self, ChessBoardManager.BoardPos(self.pos.x, self.pos.y + pawnDir[self.color.value]), Move.MoveType.NORMAL));
            
            if self.pos.y == pawnStartPosY[self.color.value]: #only if the pawn still is on its starting square we'll check if a double pawn move is possible
                #now we check if the pawn can perform a double move, notice that it can only ever do so, if it also can perform a single move
                pieceTwoSquaresInFront =  chessBoard.getPieceAtPos(ChessBoardManager.BoardPos(self.pos.x, self.pos.y + pawnDir[self.color.value] * 2)); #get the piece two squares in front of the pawn
                if pieceTwoSquaresInFront is None: #if there is no piece two squares in front of the pawn, add the move to the moves list
                    moves.append(Move(self, ChessBoardManager.BoardPos(self.pos.x, self.pos.y + pawnDir[self.color.value] * 2), Move.MoveType.DOUBLEPAWN));
            
        
        
        return moves; #return the calculated moves
    
    
    
class King(ChessPiece):
    def __init__(self, pos: ChessBoardManager.BoardPos, color: Color) -> None:
        super().__init__(pos, color, "k");
        
    def getMoves(self, chessBoard: ChessBoardManager.ChessBoard) -> list:
        
        moves = [Move(self, ChessBoardManager.BoardPos(self.pos.x - 1, self.pos.y - 1), Move.MoveType.NORMAL),
                 Move(self, ChessBoardManager.BoardPos(self.pos.x - 1, self.pos.y + 0), Move.MoveType.NORMAL),
                 Move(self, ChessBoardManager.BoardPos(self.pos.x - 1, self.pos.y + 1), Move.MoveType.NORMAL),
                 Move(self, ChessBoardManager.BoardPos(self.pos.x + 0, self.pos.y + 1), Move.MoveType.NORMAL),
                 Move(self, ChessBoardManager.BoardPos(self.pos.x + 1, self.pos.y + 1), Move.MoveType.NORMAL),
                 Move(self, ChessBoardManager.BoardPos(self.pos.x + 1, self.pos.y + 0), Move.MoveType.NORMAL),
                 Move(self, ChessBoardManager.BoardPos(self.pos.x + 1, self.pos.y - 1), Move.MoveType.NORMAL),
                 Move(self, ChessBoardManager.BoardPos(self.pos.x + 0, self.pos.y - 1), Move.MoveType.NORMAL),
                 ]; #this list will later be returned and stores all the moves theoraticly possible for the king, the ones actually invalid for different reasons, will be deleted throughout this method
        
        moves = getPossibleMovesOutOf(chessBoard, moves); #set the moves list to be only the actuall posibble moves out of itself
        
        return moves; #return the calculated moves
    
    
    
class Knight(ChessPiece):
    def __init__(self, pos: ChessBoardManager.BoardPos, color: Color) -> None:
        super().__init__(pos, color, "n");
        
    def getMoves(self, chessBoard: ChessBoardManager.ChessBoard) -> list:
        
        moves = [Move(self, ChessBoardManager.BoardPos(self.pos.x - 2, self.pos.y + 1), Move.MoveType.NORMAL),
                 Move(self, ChessBoardManager.BoardPos(self.pos.x - 1, self.pos.y + 2), Move.MoveType.NORMAL),
                 Move(self, ChessBoardManager.BoardPos(self.pos.x + 1, self.pos.y + 2), Move.MoveType.NORMAL),
                 Move(self, ChessBoardManager.BoardPos(self.pos.x + 2, self.pos.y + 1), Move.MoveType.NORMAL),
                 Move(self, ChessBoardManager.BoardPos(self.pos.x + 2, self.pos.y - 1), Move.MoveType.NORMAL),
                 Move(self, ChessBoardManager.BoardPos(self.pos.x - 1, self.pos.y - 2), Move.MoveType.NORMAL),
                 Move(self, ChessBoardManager.BoardPos(self.pos.x + 1, self.pos.y - 2), Move.MoveType.NORMAL),
                 Move(self, ChessBoardManager.BoardPos(self.pos.x - 2, self.pos.y - 1), Move.MoveType.NORMAL),
                 ]; #this list will later be returned and stores all the moves theoraticly possible for the knight, the ones actually invalid for different reasons, will be deleted throughout this method
        
        moves = getPossibleMovesOutOf(chessBoard, moves); #set the moves list to be only the actuall posibble moves out of itself
        
        return moves; #return the calculated moves




#getting moves
def getLineMoves(chessBoard: ChessBoardManager.ChessBoard, pos: ChessBoardManager.BoardPos, xIncr: int, yIncr: int) -> list: #method that'll return all the moves on a line with given gradient, in a list
    
    moves = []; #list that'll be returned and contains all the possible moves on the line with given gradient
    startPos = copy.copy(pos); #get a copy of the given position to store the startPos, which is needed to create Move classes, as we need the piece at the start position for that
    
    
    #increase the values so the startPos is not on the moves list
    pos.x += xIncr;
    pos.y += yIncr;
    
    #check foreach pos on line if valid and if so add it to the moves list
    while (pos.x < ChessBoardManager.ChessBoard.COLUMNS and pos.x >= 0 and pos.y >= 0 and pos.y < ChessBoardManager.ChessBoard.ROWS): #check if the pos currently checked for validation is even on the chessBoard
        
        piece: ChessPiece = chessBoard.getPieceAtPos(pos); #get the piece at the pos currently checked for validation
        if piece is not None: #check wether the piece variable isn't empty, if so there must be a piece at the pos currently checked for validation
            if piece.color == chessBoard.getPieceAtPos(startPos).color: #check if the piece at the pos currently checked for validation has the same color as the piece we are getting thte lineMoves for
                break; #break out of the while loop, as we can't move on a square with same colored pieces
            else: #the piece at the pos currently checked for validation must have a different color, then the piece we get the lineMoves for
                moves.append(Move(chessBoard.getPieceAtPos(startPos), copy.copy(pos), Move.MoveType.NORMAL)); #add the move, as it is valid, add a copy of the pos to the move, a reference would be modified throughout the for loop, add the move to the later returned moves list, the move type is normal, as this is just a normal line move
                break; #as you can not continue moving on the line, after crossing a piece, break out of the while loop
        
        moves.append(Move(chessBoard.getPieceAtPos(startPos), copy.copy(pos), Move.MoveType.NORMAL)); #add a copy of the pos to the move, a reference would be modified throughout the for loop, add the move to the later returned moves list, the move type is normal, as this is just a normal line move
        
        pos.x += xIncr;
        pos.y += yIncr;
        
        
    return moves; #finally return the moves list

def getPossibleMovesOutOf(chessBoard: ChessBoardManager.ChessBoard, moves: list): #this method returns a copy of given list modified, to conatin only the actually valid moves out of the given theoretically possible ones
    
    checkedMoves = copy.copy(moves); #this list will later be returned, it is a copy of the given moves list, from which the actually invalid moves will be deleted throughout this method
    
    for move in moves:
            if not ChessBoardManager.IsPosValid(move.moveTo): #if the move actually leads out of the board remove it 
                checkedMoves.remove(move); #remove the invalid move from the checkedMoves list
                continue; #continue with the next move, so the checks below this are not executed
            
            piece: ChessPiece = chessBoard.getPieceAtPos(move.moveTo); #get the piece at the move.moveTo pos currently checked for validation
            if piece is not None: #check wether the piece variable isn't empty, if so there must be a piece at the move.moveTo pos currently checked for validation
                if piece.color == move.pieceToMove.color: #check if the piece at the move.moveTo pos currently checked for validation has the same color as this piece, if so it's invalid, so remove it
                    checkedMoves.remove(move); #remove the invalid move from the checkedMoves list
                    continue; #continue with the next move, so the checks below this are not executed
                
    return checkedMoves; #return the new list, that contains all the actually valid moves, out of the given moves list


class Move: #class that stores move endPos and moveType aswell as the piece to move, the move Type is quite important for performing moves like en passant and castling
    
    class MoveType(Enum): #enum that represents the MoveType of the chessPiece
        NORMAL = 0; #by normal chess move that does not fall into the following categories
        DOUBLEPAWN = 1; #move performed when a pawn moves 2 squares, this is needed for calculating en passant moves
        EN_PASSANT = 2; #google en passant, needed to perform a given en passant move properly
        CASTLING = 3; #any castling move, needed to perform a given castling move properly
    
    
    def __init__(self, piece: ChessPiece, moveTo: ChessBoardManager.BoardPos, moveType: MoveType) -> None:
        
        self.pieceToMove = piece; #the piece that'll be moved, when this move was performed
        self.moveTo = moveTo; #the position the given piece moves to
        self.moveType = self.MoveType(moveType); #the type of move


def performMove(chessBoard: ChessBoardManager.ChessBoard, move: Move): #method that'll perform given move
    
    if move.moveType == Move.MoveType.NORMAL or Move.MoveType.DOUBLEPAWN: #if it is normal move or a DOUBLEPAWN move (moves that do not need any special kind of movmement), we'll just move the piece to the moveTo position, aswell as removing piece at the moveTo position, as it gets taken
        
        #remove any piece at the moveTo position, as the pieceToMove will take this, this has to be run before the pieceToMove is moved to avoid deliting the pieceToMove instead
        piece: ChessPiece = chessBoard.getPieceAtPos(move.moveTo); #try to get the piece at the move to position
        if piece is not None: #if there was a piece at the moveTo position, remove it from the chessBoard.pieces list, so it got taken
            chessBoard.pieces.remove(piece); #remove piece from the chessBoard.pieces list, so it got taken
        
        move.pieceToMove.pos = move.moveTo; #move the pieceToMove to the moveTo position
