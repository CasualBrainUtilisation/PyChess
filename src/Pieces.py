#class that'll handle everything related to chess pieces

from enum import Enum; #so we can use Enums, used for piece color
from ChessBoardManager import *; #import the ChessBoardManager class, so we have acces to BoardPos ect.

class Color(Enum): #enum used to store a piece's color
        White = 0;
        Black = 1;
    
    
class ChessPiece:
    
    def __init__(self, pos: BoardPos, color: Color) -> None:
        
        self.pos = pos; #this stores the piece position on the chessBoard
        self.color = color; #set the color of the piece
        

class Rook(ChessPiece):
    def __init__(self, pos: BoardPos, color: Color) -> None:
        super().__init__(pos, color);
        
    def getMoves(chessBoard: ChessBoard) -> list:
        #TODO logic to get moves
        return [super().pos];