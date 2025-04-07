import pygame
from circleshape import CircleShape
from constants import*



class Shot(CircleShape):
    def __init__(self, x, y, velocity):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = velocity

     # draw the bullets  
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width= 2)

    # moves in a straight line at a constant speed each frame 
    def update(self, dt):
        self.position += self.velocity * dt
