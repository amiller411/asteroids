import pygame
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        return super().__init__(x, y, radius)
            
    def draw(self, screen):
        return pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.move(dt)

    def move(self, dt):
        # Move forward in a straight line at constant speed
        self.position +=  self.velocity * dt