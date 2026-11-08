import pygame
import random
from circleshape import CircleShape
from constants import *
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
        self.rotation = 0
        self.rotation_speed = random.uniform(-20, 20)
        self.sides = ASTEROID_SIDES
        self.modify = []

        for i in range(0, self.sides):
            self.modify.append(random.uniform(-10,2))

    def polygon(self) -> list[pygame.Vector2]:
        vectors = []
        angle = 360 / self.sides
        for i in range(0, self.sides):
            forward = pygame.Vector2(0, 1).rotate(self.rotation + (angle * i))
            vectors.append(self.position + forward * (self.radius + self.modify[i]))
        return vectors
           
    def rotate(self, dt: float) -> None:
        self.rotation += self.rotation_speed * dt

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.polygon(screen, "black", self.polygon(), 0)
        pygame.draw.polygon(screen, "white", self.polygon(), LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt
        self.rotate(dt)

        if (
            self.position.x < -SCREEN_WARP * 3
            or self.position.x > SCREEN_WIDTH + SCREEN_WARP * 3
            or self.position.y < -SCREEN_WARP * 3
            or self.position.y > SCREEN_HEIGHT + SCREEN_WARP * 3
        ):
            self.kill()

    def split(self) -> None:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        new_angle = random.uniform(20, 50)
        new_velocity1 = self.velocity.rotate(new_angle)
        new_velocity2 = self.velocity.rotate(-new_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = new_velocity1 * 1.2
        asteroid2.velocity = new_velocity2 * 1.2
