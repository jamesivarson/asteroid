import circleshape
import pygame
from constants import *

class Player(circleshape.CircleShape):
    def __init__(self, x, y, PLAYER_RADIUS, shots_group):
        # Call the parent constructor (CircleShape)
        super().__init__(x, y, PLAYER_RADIUS)
        self.shots_group = shots_group
        self.rotation = 0  # Initialize rotation
        self.last_shot_time = 0


        # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), width=2)

    def rotate(self, dt):
        rotation = PLAYER_TURN_SPEED * dt
    
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotation -= PLAYER_TURN_SPEED * dt
        if keys[pygame.K_d]:
            self.rotation += PLAYER_TURN_SPEED * dt
        
        if keys[pygame.K_w]:
            self.move(dt)
        
        if keys[pygame.K_s]:
            self.move(-dt)

        if keys[pygame.K_SPACE]:
            self.shoot()

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        current_time = pygame.time.get_ticks()  # Get the current time in milliseconds
        cooldown_time = PLAYER_SHOOT_COOLDOWN * 1000
    
        if current_time - self.last_shot_time >= cooldown_time:
            forward = pygame.Vector2(0, 1).rotate(self.rotation)
            shot_velocity = forward * PLAYER_SHOOT_SPEED
            new_shot = circleshape.Shot(self.position, shot_velocity)  # Pass position as a vector

            self.shots_group.add(new_shot)  # Add the shot to the group

            # Update the last shot time
            self.last_shot_time = current_time