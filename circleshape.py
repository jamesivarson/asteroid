import pygame
from constants import *

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass
    def is_collisions(self, other_shape):
        # Check if the distance between the two shapes is less than the sum of their radii
        distance = self.position.distance_to(other_shape.position)
        return distance < (self.radius + other_shape.radius)
    
class Shot(CircleShape, pygame.sprite.Sprite):
    def __init__(self, position, velocity):
        # Initialize the parent classes
        super().__init__(position.x, position.y, SHOT_RADIUS)
        pygame.sprite.Sprite.__init__(self)

        # Set velocity
        self.velocity = velocity

        # Create the visual representation (image)
        self.image = pygame.Surface((SHOT_RADIUS * 2, SHOT_RADIUS * 2), pygame.SRCALPHA)  # Transparent surface
        pygame.draw.circle(self.image, (255, 255, 255), (SHOT_RADIUS, SHOT_RADIUS), SHOT_RADIUS)

        # Define the rect for positioning
        self.rect = self.image.get_rect(center=(self.position.x, self.position.y))

    def update(self, dt):
        # Update position based on velocity
        self.position += self.velocity * dt

        # Sync the rect's center with the updated position
        self.rect.center = (self.position.x, self.position.y)

        # Check if the shot is off-screen and remove it
        if (
            self.position.x < 0 or self.position.x > SCREEN_WIDTH or
            self.position.y < 0 or self.position.y > SCREEN_HEIGHT
        ):
            self.kill()  # Remove the shot from the sprite group