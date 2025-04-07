import pygame
from circleshape import CircleShape
from constants import*
from shot import Shot



# create Player class that inherits from CircleShape
class Player(CircleShape):
    def __init__(self, x, y):
        
        #call parent class constructor and pass in PLAYER_RADIUS
        super().__init__(x, y, PLAYER_RADIUS)
        
        #create field "rotation" set to 0
        self.rotation = 0

        #adding timer for shooting cooldown
        self.shoot_timer = 0
   
    # paste in the player class this triangle method 
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        # sub-classes must override the draw method of CircleShape.
        # It should take the screen object as a parameter, and call pygame.draw.polygon
        #self.screen = screen
        pygame.draw.polygon(screen, "white", self.triangle(), width=2)

    
    # add rotate feature
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    # add move feature
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    
    
    def shoot(self):
        # limit shooting by using the timer
        if self.shoot_timer <= 0:
            
            # Create a direction vector pointing "up" (0, 1) for pygame coordinates
            # Rotate it to match the player's direction
            direction = pygame.Vector2(0, 1).rotate(self.rotation)
            
            # Scale it by the shoot speed
            velocity = direction * PLAYER_SHOOT_SPEED
            
            # Create a new shot
            Shot(self.position.x, self.position.y, velocity)

            # reset the timer for each shot
            self.shoot_timer = PLAYER_SHOOT_COOLDOWN



    #updates movement of player
    def update(self, dt):
        
        # decrease shoot timer by dt every frame
        if self.shoot_timer > 0:
            self.shoot_timer -= dt
        
        
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