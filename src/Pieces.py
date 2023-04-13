#class that'll handle everything related to chess pieces

from enum import Enum; #so we can use Enums, used for piece color
from ChessBoardManager import *; #import the ChessBoardManager class, so we have acces to BoardPos ect.

class Color(Enum): #enum used to store a piece's color
        White = 0;
        Black = 1;
    
    
class ChessPiece:
    
    def __init__(self, pos: BoardPos, color: Color, name: str) -> None:
        
        self.pos = pos; #this stores the piece position on the chessBoard
        self.color = color; #set the color of the piece
        
        self.name = name;
        

class Rook(ChessPiece):
    def __init__(self, pos: BoardPos, color: Color) -> None:
        super().__init__(pos, color, "rook");
        
    def getMoves(chessBoard: ChessBoard) -> list:
        #TODO logic to get moves
        return [super().pos];
    
    
    
class Bishop(ChessPiece):
    def __init__(self, pos: BoardPos, color: Color) -> None:
        super().__init__(pos, color, "bishop");
        
    def getMoves(chessBoard: ChessBoard) -> list:
        #TODO logic to get moves
        return [super().pos];
    
    

class Queen(ChessPiece):
    def __init__(self, pos: BoardPos, color: Color) -> None:
        super().__init__(pos, color, "queen");
        
    def getMoves(chessBoard: ChessBoard) -> list:
        #TODO logic to get moves
        return [super().pos];  
    
    
    
class Pawn(ChessPiece):
    def __init__(self, pos: BoardPos, color: Color) -> None:
        super().__init__(pos, color, "pawn");
        
    def getMoves(chessBoard: ChessBoard) -> list:
        #TODO logic to get moves
        return [super().pos]; 
    
    
    
class King(ChessPiece):
    def __init__(self, pos: BoardPos, color: Color) -> None:
        super().__init__(pos, color, "king");
        
    def getMoves(chessBoard: ChessBoard) -> list:
        #TODO logic to get moves
        return [super().pos];
    
    
    
class Knight(ChessPiece):
    def __init__(self, pos: BoardPos, color: Color) -> None:
        super().__init__(pos, color, "knight");
        
    def getMoves(chessBoard: ChessBoard) -> list:
        #TODO logic to get moves
        return [super().pos];
