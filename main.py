import pygame
from constants import *
from player import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    print("Starting asteroids!")
    # print(SCREEN_WIDTH)
    # print(SCREEN_HEIGHT)
    running = True
    timeclock = pygame.time.Clock()
    dt = 0
    player_object = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)  
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        player_object.draw(screen)
        pygame.display.flip()
        dt = timeclock.tick(60) / 1000
         
        
    
if __name__ == "__main__":
    main()
