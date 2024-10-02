from circleshape import CircleShape
from constants import *
import pygame
from shot import Shot


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)

        self.rotation = 0
        self.timer = 0
        self.velocity = pygame.Vector2(0, 0) * 0.8
    
    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
    
    def rotate(self, dt):
        self.rotation = self.rotation + (PLAYER_TURN_SPEED * dt)

    def update(self, dt):
        self.timer = self.timer - dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
            
        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_w]:
            self.move(dt)
        
        if keys[pygame.K_s]:
            self.move(-dt)
        
        if keys[pygame.K_SPACE]:
            self.shoot()

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.sliding_factor = min(0.8 - 0.01 * dt, 0.2)
        self.position += forward * PLAYER_SPEED * dt * (1 - self.sliding_factor)

    def shoot(self):
        if self.timer < 0:
            newShot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
            shotVelocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
            newShot.velocity = shotVelocity
            self.timer = PLAYER_SHOOT_COOLDOWN

