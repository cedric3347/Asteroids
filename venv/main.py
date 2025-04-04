import pygame
from constants import*
from player import*


def main():
    # initialize py.game
    pygame.init()
        
    #create GUI window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        
    #create Time object
    clock = pygame.time.Clock()
    dt = 0

    #instantiate Player object
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))

    #create game loop
    while True:
        
        # check if user closed window/make close button work        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # update movment
        player.update(dt)
        
        # fill screen with solid "black" color
        screen.fill("black")

        # re-render the player on the screen each frame,
        player.draw(screen)

        # render/update display
        pygame.display.flip()
        
        # limit framerate to 60fps and update delta time
        dt = clock.tick(60) / 1000
    
        



if __name__ == "__main__":
    main()