import pygame
from constants import*
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    # initialize py.game
    pygame.init()

    #set up groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    # set groups as containers
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
        
    #create GUI window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        
    #create Time object
    clock = pygame.time.Clock()
    dt = 0

    #instantiate Player object
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    
    #instantiate asteroidfield
    asteroidfield = AsteroidField()

    #create game loop
    while True:
        
        # check if user closed window/make close button work        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # update movment
        for sprite in updatable:
            sprite.update(dt)
        
        # fill screen with solid "black" color
        screen.fill("black")

        # re-render the player on the screen each frame
        for sprite in drawable:
            sprite.draw(screen)

        # render/update display
        pygame.display.flip()
        
        # limit framerate to 60fps and update delta time
        dt = clock.tick(60) / 1000
    
        



if __name__ == "__main__":
    main()