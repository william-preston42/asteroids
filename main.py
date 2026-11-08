import sys
import pygame
from asteroid import Asteroid
from constants import * 
import game_info
from logger import log_state, log_event
from player import *
from asteroidfield import AsteroidField
from game_info import *
from textengine import *

def main():
    pygame.init()
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    score = Score(20, 20)
    current_score: int = 0

    clock = pygame.time.Clock()
    dt = 0.0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group() 
    shots = pygame.sprite.Group()
    lives = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)
    Lives.containers = (lives,)

    life = {
        1: Lives(30, 60, LIVES_RADIUS),
        2: Lives(60, 60, LIVES_RADIUS),
        3: Lives(90, 60, LIVES_RADIUS),
    }

    player = Player((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2), PLAYER_RADIUS)
    asteroidfield = AsteroidField()


    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    return
        screen.fill("black")

        for drawing in drawable:
            drawing.draw(screen)
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player, 0):
                if player.lives > 0:
                    log_event("player_hit")
                    life[player.lives].kill()
                    player.death()
                    for asteroid in asteroids:
                        if asteroid.collides_with(player, DEATH_RADIUS):
                            asteroid.kill()
                if player.lives == 0:
                    log_event("player_killed")
                    print("Game over!")
                    print(f"Final score: {current_score}")
                    sys.exit()

        for asteroid in asteroids:
            for shot in shots:
                if shot.collides_with(asteroid, 0):
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.split()
                    current_score += (80 - asteroid.radius)

        score.player_score(current_score, screen)
        for live in lives:
            live.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
