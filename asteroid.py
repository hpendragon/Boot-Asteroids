# asteroid.py
import pygame
import random
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from circleshape import CircleShape
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(
            screen,
            "white",
            self.position,
            self.radius,
            LINE_WIDTH
        )
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        # Always destroy this asteroid
        self.kill()
        
        # Check if asteroid is too small to split
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
            
        # Log the split event
        log_event("asteroid_split")
        
        # Calculate new properties
        split_angle = random.uniform(20, 50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        # Create velocity vectors for new asteroids
        vel1 = self.velocity.rotate(split_angle)
        vel2 = self.velocity.rotate(-split_angle)
        
        # Create new asteroids
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        
        # Set velocities (scaled up by 1.2)
        asteroid1.velocity = vel1 * 1.2
        asteroid2.velocity = vel2 * 1.2
