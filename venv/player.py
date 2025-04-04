from circleshape import*
from constants import*



# create Player class that inherits from CircleShape
class Player(CircleShape):
    def __init__(self, x, y):
        
        #call parent class constructor and pass in PLAYER_RADIUS
        super().__init__(x, y, PLAYER_RADIUS)
        
        #create field "rotation" set to 0
        self.rotation = 0

    # paste in the player class this triangle methodASUS ROG Swift PG348Q 
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
    
    
    
    #updates movement of player
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)