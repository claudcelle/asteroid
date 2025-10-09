from circleshape import CircleShape
from asteroid import Asteroid
from constants import *
import pygame 

class Player(CircleShape):
    def __init__(self, x, y, radius=PLAYER_RADIUS):
        super().__init__(x, y, radius)
        self.rotation = 0
        self.shoot_timer = 0

    def __repr__(self):
        a,b,c = self.triangle()
        return f"Player(x={self.position.x:.2f}, y={self.position.y:.2f}, radius={self.radius}, rotation={self.rotation:.2f}, velocity: {self.velocity:.2f}, vertices: {a,b,c})"

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self,screen,color = "green",width=OBJECTS_WIDTH):
        pygame.draw.polygon(surface = screen,
                            color=color,
                            points=self.triangle(),
                            width=width)
        
    def rotate(self,dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self,dt):
        self.position += pygame.Vector2(0,1).rotate(self.rotation)*PLAYER_SPEED*dt

    def shoot(self):
        a,b,c = self.triangle()
        shot = Shot(a.x,a.y)
        # shot = Shot(self.position.x ,
        #             self.position.y + self.radius,
        #             )
        shot.velocity = pygame.Vector2(0,1).rotate(self.rotation)*PLAYER_SHOOT_RATE

        
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] or keys[pygame.K_UP]:
        #     # * moves forward
            self.move(dt)
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        #     #* moves backward
            self.move(-dt)
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            #* turn left
            if keys[pygame.K_s]:
                self.rotate(dt)
            else:
                self.rotate(-dt)
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            # * turn right
            if keys[pygame.K_s]:
                self.rotate(-dt)
            else:
                self.rotate(dt)
        if keys[pygame.K_SPACE]:
            if self.shoot_timer>0:
                self.shoot_timer-=dt
            else:    
                self.shoot()
                self.shoot_timer = PLAYER_SHOOT_COOLDOWN
            # self.


class Shot(Asteroid):
    
    def __init__(self, x, y, radius = SHOT_RADIUS):
        super().__init__(x, y, radius)

    


player = Player(1,2,4)
player.rotation=45
player.velocity=4321
print(player)
