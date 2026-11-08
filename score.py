import pygame
from textengine import Text

class Score(Text):
    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y)
        self.score = 0

    def player_score(self, current_score: int, screen: pygame.Surface) -> None:
        self.draw_text(f"Score: {current_score}", screen)

class Lives(Text):
    def __init__(self, x: float, y: float, radius) -> None:
        super().__init__(x, y)
        self.radius = radius

    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1)
        right = pygame.Vector2(0, 1).rotate(90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - (forward / 2) * self.radius
        d = self.position - forward * self.radius + right
        return [a, b, c, d]

    def draw_graphic(self, screen) -> None:
        
