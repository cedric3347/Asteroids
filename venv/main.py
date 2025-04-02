import pygame
from constants import*


def main():
    # initialize py.game
    pygame.init()
        
    #create GUI window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        
    #create Time object
    clock = pygame.time.Clock()
    dt = 0

    #create game loop
    while True:
        
        # check if user closed window/make close button work        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # fill screen with solid "black" color
        screen.fill("black")
        
        # Render/update display
        pygame.display.flip()
        
        # Update delta time
        dt = clock.tick(60) / 1000
    
        










if __name__ == "__main__":
    main()