import pygame
from circleshape import CircleShape
from constants import *
import random

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

    def split(self):
        self.kill()

        # If it is already a small asteroid
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        # Split into medium and small asteroids
        random_velocity = random.uniform(20, 50)

        new_velocity_a = self.velocity.rotate(random_velocity)
        new_velocity_b = self.velocity.rotate(-random_velocity)
        old_radius = self.radius
        self.radius = old_radius - ASTEROID_MIN_RADIUS
        
        # Create new asteroid objects
        a = Asteroid(self.position[0], self.position[1], self.radius)
        b = Asteroid(self.position[0], self.position[1], self.radius)

        a.velocity = new_velocity_a * 1.2
        b.velocity = new_velocity_b
