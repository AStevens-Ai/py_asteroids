from circleshape import CircleShape
import pygame
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, surface):
        pygame.draw.circle(surface, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position = self.position + (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle =  random.uniform(20, 50)
            vectorOne = self.velocity.rotate(random_angle)
            vectorTwo = self.velocity.rotate(-random_angle)
            newRadius = self.radius - ASTEROID_MIN_RADIUS
            asteroidOne = Asteroid(self.position.x, self.position.y, newRadius)
            asteroidTwo = Asteroid(self.position.x, self.position.y, newRadius)

            asteroidOne.velocity = vectorOne * 1.2
            asteroidTwo.velocity = vectorTwo * 1.2