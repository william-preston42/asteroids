import pygame
import asteroid
from circleshape import CircleShape
from constants import *
from shot import Shot

class Player(CircleShape):
    def __init__(self, x: float, y: float, PLAYER_RADIUS: int) -> None:
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_timer = 0
        self.lives = 3

    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - (forward / 2) * self.radius
        d = self.position - forward * self.radius + right
        return [a, b, c, d]

    def triangle_fire(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position - (forward / 2) * self.radius
        b = self.position - (forward / 1.5) * self.radius - (right / 2.6)
        c = self.position - (forward * 1.5) * self.radius
        d = self.position - (forward / 1.5) * self.radius + (right / 2.6)
        return [a, b, c, d]

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)
        if pygame.key.get_pressed()[pygame.K_w]:
            pygame.draw.polygon(screen, "white", self.triangle_fire(), LINE_WIDTH)

    def rotate(self, dt: float) -> None:
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt: float) -> None:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)

        if not keys[pygame.K_w]:
            self.velocity -= (self.velocity / 2) * dt
        self.position += self.velocity * dt

        self.shoot_timer -= dt
        if keys[pygame.K_SPACE]:
            self.shoot()

        if self.position.x < -SCREEN_WARP:
            self.position.x = SCREEN_WIDTH + SCREEN_WARP
        if self.position.x > SCREEN_WIDTH + SCREEN_WARP:
            self.position.x = -SCREEN_WARP
        if self.position.y < -SCREEN_WARP:
            self.position.y = SCREEN_HEIGHT + SCREEN_WARP
        if self.position.y > SCREEN_HEIGHT + SCREEN_WARP:
            self.position.y = - SCREEN_WARP

    def move(self, dt: float) -> None:
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_ACCELERATION * dt
        self.velocity += rotated_with_speed_vector
        if self.velocity.length() != 0:
            self.velocity.clamp_magnitude_ip(MAX_PLAYER_SPEED)

    def shoot(self) -> None:
        if self.shoot_timer > 0:
            return
        self.shoot_timer = PLAYER_SHOOT_COOLDOWN_SECONDS
        shot = Shot(self.position.x, self.position.y)
        unit_vector = pygame.math.Vector2(0,1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SHOOT_SPEED
        shot.velocity = rotated_with_speed_vector

    def death(self) -> None:
        self.lives -= 1
        self.position = pygame.Vector2((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2))
        self.velocity = pygame.Vector2(0, 0)
        self.rotation = 0
