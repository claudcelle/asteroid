# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player, Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys

def main():
    # print("Starting Asteroids!" )
    # print(f"Screen width: {SCREEN_WIDTH}")
    # print(f"Screen height: {SCREEN_HEIGHT}")
    
    pygame.init() 
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0 
    
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatables,drawables)
    Asteroid.containers = (updatables,drawables,asteroids)
    AsteroidField.containers = (updatables)
    Shot.containers = (updatables,drawables)


    player_1 = Player(x = SCREEN_WIDTH/2,
                      y = SCREEN_HEIGHT/2)
    # print(player_1)
    asteroid_field = AsteroidField()
    while True: 
        """ Allows to close the window with close button"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return sys.exit(0)
        screen.fill(color="black")
        # player_1.update(dt=dt)
        # for updatable in updatables:
        updatables.update(dt=dt)
        # player_1.shoot_timer -= dt

        for asteroid in asteroids:
            if asteroid.check_collision(player_1):
                print("Game Over!")
                return sys.exit(0)
        # player_1.draw(screen=screen)
        for drawable in drawables:
            drawable.draw(screen=screen)
        pygame.display.flip()
        dt = clock.tick(60)/1000 #*.tick() pause game loop until 1/60th of a second has passed. Returns time passed since last call (dt). Divide by 1000 (milliseconds -> seconds)


if __name__ == "__main__":
    main()
