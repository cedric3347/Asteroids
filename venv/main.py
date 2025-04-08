import sys
import pygame
from constants import*
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import hud



def main():
    # initialize py.game
    pygame.init()

    # set up groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    

    # set groups as containers
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)
        
    # create GUI window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        
    # create Time object
    clock = pygame.time.Clock()
    dt = 0

    # instantiate Player object
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    
    # instantiate asteroidfield
    asteroidfield = AsteroidField()

    # instantiate Player Lives
    lives = PLAYER_LIVES

    # instantiate score
    score = PLAYER_SCORE

    # create game loop
    while True:
        
        # check if user closed window/make close button work        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # update movment
        for sprite in updatable:
            sprite.update(dt)

        # check for asteroid collision with ship
        for asteroid in asteroids:
            if player.collision_check(asteroid):
                player.kill()
                lives -= 1
                player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
            
            if lives <= 0:
                sys.exit("Game over!")
            
            #check for bullet collision with asteroid and destroy them if they collide
            for bullet in shots:
                if asteroid.collision_check(bullet):
                    bullet.kill()
                    # add score based on asteroid size
                    if asteroid.radius > ASTEROID_MIN_RADIUS * 2:  
                        score += 100
                    elif asteroid.radius > ASTEROID_MIN_RADIUS:  
                        score += 150
                    else:      
                        score += 200

                    # splits asteroids
                    asteroid.split()

        
        # fill screen with solid "black" color
        screen.fill("black")
        
        # draw lives on screen
        hud.draw_lives(screen, lives)

        # draw score on screen
        hud.draw_score(screen, score)

       
        # re-render the player on the screen each frame
        for sprite in drawable:
            sprite.draw(screen)

        # render/update display
        pygame.display.flip()
        
        # limit framerate to 60fps and update delta time
        dt = clock.tick(60) / 1000      



if __name__ == "__main__":
    main()