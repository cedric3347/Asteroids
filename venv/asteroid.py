import pygame
from circleshape import CircleShape
from constants import*
import random




class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
       

     # draw the asteroid   
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width= 2)

    # moves in a straight line at a constant speed each frame 
    def update(self, dt):
        self.position += self.velocity * dt

    
    def split(self):
        #destroys asteroid
        self.kill()

        #spawns smaller asteroids if less than or equal to ASTEROID_MIN_RADIUS
        if self.radius <= ASTEROID_MIN_RADIUS:
           return
        
        random_angle  = random.uniform(20, 50)
        
        new_velocity1 = self.velocity.rotate(random_angle)
        new_velocity2 = self.velocity.rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        #asteroid 1
        spawn_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        spawn_asteroid1.velocity = new_velocity1 * 1.2
        
        #asteroid 2
        spawn_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        spawn_asteroid2.velocity = new_velocity2 * 1.2



