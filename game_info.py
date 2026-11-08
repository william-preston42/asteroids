import random
import pygame
from circleshape import CircleShape
from textengine import Text
from constants import LINE_WIDTH

class Score(Text):
    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y)
        self.score = 0

    def player_score(self, current_score: int, screen: pygame.Surface) -> None:
        self.draw_text(f"Score: {current_score}", screen)

class Lives(CircleShape):
    def __init__(self, x: float, y: float, radius: int) -> None:
        super().__init__(x, y, radius)
   
    def draw(self, screen: pygame.Surface) -> None:
        forward = pygame.Vector2(0, 1)
        right = pygame.Vector2(0, 1).rotate(90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - (forward / 2) * self.radius
        d = self.position - forward * self.radius + right
        shape = [a, b, c, d]
        pygame.draw.polygon(screen, "white", shape, LINE_WIDTH)
