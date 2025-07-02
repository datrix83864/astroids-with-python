import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x, y, velocity):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = velocity
        
    def update(self, dt):
        # Move the shot based on its velocity
        self.position += self.velocity * dt
        
    def draw(self, screen):
        # Draw the shot as a circle
        pygame.draw.circle(screen, (255, 0, 0), (int(self.position.x), int(self.position.y)), self.radius)