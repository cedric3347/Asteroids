import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

# adds collision detection.If distance is less than or equal to radius_1 + radius_2, the circles are colliding. If not, they aren't.
    def collision_check(self, other_object):
        distance = self.position.distance_to(other_object.position)
        radius_sums = self.radius + other_object.radius
        if distance <= radius_sums:
            return True
        else:
            return False
