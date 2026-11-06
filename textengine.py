import pygame
import sys

class Text:
    def __init__(self, x: float, y: float) -> None:
        self.position: pygame.Vector2 = pygame.Vector2(x, y)
        self.font = pygame.font.SysFont("Arial", 18)

    def draw(self, text, screen) -> None:
        drawn_text = pygame.font.Font.render(self.font, text, True, "white") 
        screen.blit(drawn_text, self.position)
