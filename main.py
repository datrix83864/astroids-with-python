# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()  # Initialize all imported pygame modules
    start_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_speed = pygame.time.Clock()
    dt = 0.0
    
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updateable, drawable)
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updateable, drawable)
    
    AsteroidField.containers = (updateable)
    asteroid_field = AsteroidField()
    
    shots = pygame.sprite.Group()
    Shot.containers = (shots, updateable, drawable)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        start_surface.fill((0,0,0))
        updateable.update(dt)
        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game Over!")
                sys.exit(0)
        for asteroid in asteroids:
            for shot in shots:
                # Check for collision between asteroid and shot
                if asteroid.collision(shot):
                    asteroid.split()
                    shot.kill()
        for drawing in drawable:
            drawing.draw(start_surface)
        pygame.display.flip()
        dt = game_speed.tick(60) / 1000.0  # Convert milliseconds to seconds

if __name__ == "__main__":
    main()