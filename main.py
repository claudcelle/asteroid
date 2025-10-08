# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player

def main():
    # print("Starting Asteroids!" )
    # print(f"Screen width: {SCREEN_WIDTH}")
    # print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init() 
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0 
    player_1 = Player(x = SCREEN_WIDTH/2,
                      y = SCREEN_HEIGHT/2)
    while True: 
        """ Allows to close the window with close button"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color="black")
        player_1.update(dt=dt)
        player_1.draw(screen=screen)

        pygame.display.flip()
        dt = clock.tick(60)/1000 #*.tick() pause game loop until 1/60th of a second has passed. Returns time passed since last call (dt). Divide by 1000 (milliseconds -> seconds)


if __name__ == "__main__":
    main()
