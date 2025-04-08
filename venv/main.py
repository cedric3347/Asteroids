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

    # instantiate "game over" variable
    game_over = False

    # font for game over screen
    game_over_font = pygame.font.SysFont(None, 64)
    instructions_font = pygame.font.SysFont(None, 32)

    # create game loop
    while True:
        
        # check if user closed window/make close button work        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
            if game_over and event.type == pygame.MOUSEBUTTONDOWN:
                # reset game state
                game_over = False
                lives = PLAYER_LIVES
                score = PLAYER_SCORE
                player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
                
                # clear asteroid field and repopulate
                for asteroid in asteroids:
                    asteroid.kill()
                asteroidfield = AsteroidField()

        if not game_over:    
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
                    game_over = True
                
                # check for bullet collision with asteroid and destroy them if they collide
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

        if not game_over:
        
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
        
        else:
            # draws game over screen
            game_over_text = game_over_font.render("GAME OVER", True, ("red"))
            score_text = instructions_font.render(f"Final Score: {score}", True, ("white"))
            restart_text = instructions_font.render("Click anywhere to restart", True, ("white"))
            
            # center the text on screen
            game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 50))
            score_rect = score_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 10))
            restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 60))
            
            # draw text on screen
            screen.blit(game_over_text, game_over_rect)
            screen.blit(score_text, score_rect)
            screen.blit(restart_text, restart_rect)
            
            # update display
            pygame.display.flip()
            
            # tick the clock in game over state
            dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()