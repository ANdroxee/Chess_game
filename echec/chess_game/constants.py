import pygame
import os

#Size
Width, Height = 760,760
Rows, Cols = 8,8
Square = Width//Rows

#Colors
Bg = (47,79,79)
Black = (0,0,0)
White = (255,255,255)
beige = (245,245,220)
brown_chocolate = (210,105,30)
brown = (87,16,16)
cornsilk = (255,248,220)
Gray = (192,192,192)
Blue = (126, 189, 255)

# Pièces noires
Black_Knight = pygame.transform.scale(pygame.image.load(os.path.join("chess_game", "chess_image", "bKN.png")), (Square, Square))
Black_Bishop = pygame.transform.scale(pygame.image.load(os.path.join("chess_game", "chess_image", "bB.png")), (Square, Square))
Black_King = pygame.transform.scale(pygame.image.load(os.path.join("chess_game", "chess_image", "bK.png")), (Square, Square))
Black_pawn = pygame.transform.scale(pygame.image.load(os.path.join("chess_game", "chess_image", "bP.png")), (Square, Square))
Black_Queen = pygame.transform.scale(pygame.image.load(os.path.join("chess_game", "chess_image", "bQ.png")), (Square, Square))
Black_Rook = pygame.transform.scale(pygame.image.load(os.path.join("chess_game", "chess_image", "bR.png")), (Square, Square))
# Pièces blanches
White_Knight = pygame.transform.scale(pygame.image.load(os.path.join("chess_game", "chess_image", "wKN.png")), (Square, Square))
White_bishop = pygame.transform.scale(pygame.image.load(os.path.join("chess_game", "chess_image", "wB.png")), (Square, Square))
White_King = pygame.transform.scale(pygame.image.load(os.path.join("chess_game", "chess_image", "wK.png")), (Square, Square))
White_pawn = pygame.transform.scale(pygame.image.load(os.path.join("chess_game", "chess_image", "wp.png")), (Square, Square))
White_Queen = pygame.transform.scale(pygame.image.load(os.path.join("chess_game", "chess_image", "wQ.png")), (Square, Square))
White_Rook = pygame.transform.scale(pygame.image.load(os.path.join("chess_game", "chess_image", "wR.png")), (Square, Square))
