from circleshape import CircleShape
from constants import *
import pygame 

class Player(CircleShape):
    def __init__(self, x, y, radius=PLAYER_RADIUS):
        super().__init__(x, y, radius)
        self.rotation = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self,screen):
        pygame.draw.polygon(surface = screen,
                            color="white",
                            points=self.triangle(),
                            width=2)
        
    def rotate(self,dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self,dt):
        self.position += pygame.Vector2(0,1).rotate(self.rotation)*PLAYER_SPEED*dt
        
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
        #     # * moves forward
            self.move(dt)
        if keys[pygame.K_s]:
        #     #* moves backward
            self.move(-dt)
        if keys[pygame.K_a]:
            #* turn left
            if keys[pygame.K_s]:
                self.rotate(dt)
            else:
                self.rotate(-dt)
        if keys[pygame.K_d]:
            # * turn right
            if keys[pygame.K_s]:
                self.rotate(-dt)
            else:
                self.rotate(dt)