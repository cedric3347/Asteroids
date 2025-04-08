import pygame
from constants import SCREEN_WIDTH



 # display lives on screen 
def draw_lives(screen, lives):
    for i in range(lives):
        # Draw small ship icons in a row
        x = 20 + (i * 30)  # Space them 30 pixels apart
        y = 20
        
        # Draw a mini version of your ship at this position
        # If your ship is a triangle, something like:
        points = [(x, y-10), (x+7, y+10), (x-7, y+10)]
        pygame.draw.polygon(screen, "white", points, width=1)

 # draw the player's score on the screen
def draw_score(screen, score):
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, "white")
    screen.blit(score_text, (SCREEN_WIDTH - 150, 20))