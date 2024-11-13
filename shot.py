import pygame
from constants import *
from circleshape import CircleShape


class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.direction = pygame.Vector2(0, 1)

    def draw(self, screen):
        return pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.move(dt)

    def move(self, dt):
        # Move forward in a straight line at constant speed
        self.position +=  self.direction * self.velocity * dt