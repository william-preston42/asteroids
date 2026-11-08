import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS, LINE_WIDTH, SCREEN_WARP, SCREEN_HEIGHT, SCREEN_WIDTH

class Shot(CircleShape):
    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

        if (
            self.position.x < -SCREEN_WARP
            or self.position.x > SCREEN_WIDTH + SCREEN_WARP
            or self.position.y < -SCREEN_WARP
            or self.position.y > SCREEN_HEIGHT + SCREEN_WARP
        ):
            self.kill()
