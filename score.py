import pygame
from textengine import Text

class Score(Text):
    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y)
        self.score = 0

    def player_score(self, current_score: int, screen: pygame.Surface) -> None:
        self.draw(f"Score: {current_score}", screen)
