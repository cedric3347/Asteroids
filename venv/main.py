import sys
import pygame
from constants import*
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot



def main():
    # initialize py.game
    pygame.init()

    #set up groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    

    # set groups as containers
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)
        
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

        for asteroid in asteroids:
            if player.collision_check(asteroid):
                sys.exit("Game over!")
        
        # fill screen with solid "black" color
        screen.fill("black")

        # re-render the player on the screen each frame
        for sprite in drawable:
            sprite.draw(screen)

        # render/update display
        pygame.display.flip()
        
        # limit framerate to 60fps and update delta time
        dt = clock.tick(60) / 1000
    
         #updates movement of player
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)

    # adding space to shoot
        if keys[pygame.K_SPACE]:
            self.shoot()



if __name__ == "__main__":
    main()