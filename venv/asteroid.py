import pygame
from circleshape import CircleShape
from constants import*




class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
       

     # draw the asteroid   
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width= 2)

    # moves in a straight line at a constant speed each frame 
    def update(self, dt):
        self.position += self.velocity * dt