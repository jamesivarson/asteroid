import pygame
from constants import *
from player import Player
from asteroid import * #
from asteroidfield import AsteroidField
import circleshape
def main():
    pygame.init()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots_group = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    asteroid_field = AsteroidField()
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS, shots_group)
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000
        screen.fill((0, 0, 0))
        updatable.update(dt)
        shots_group.update(dt)
        shots_group.draw(screen)
        for asteroid in asteroids:
            if player.is_collisions(asteroid):
                print("Game over!")
                import sys
                sys.exit()
                return
        for shot in shots_group:
            for asteroid in asteroids:
                if shot.is_collisions(asteroid):
                    shot.kill()
                    asteroid.kill()
                    break
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
    print("Starting Asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)
if __name__ == "__main__":
    main()