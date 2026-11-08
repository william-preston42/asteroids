import pygame
import sys
from constants import *

class Text:
    def __init__(self, x: float, y: float) -> None:
        self.position: pygame.Vector2 = pygame.Vector2(x, y)
        self.font = pygame.font.SysFont("Monaco", 20)

    def draw_text(self, text, screen) -> None:
        drawn_text = pygame.font.Font.render(self.font, text, True, "white") 
        screen.blit(drawn_text, self.position)
