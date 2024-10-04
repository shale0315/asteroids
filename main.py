import pygame
from constants import *
from player import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    print("Starting asteroids!")
    # print(SCREEN_WIDTH)
    # print(SCREEN_HEIGHT)
    running = True
    timeclock = pygame.time.Clock()
    dt = 0
      
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatables, drawables)
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = (updatables)
    Shot.containers = (shots, updatables, drawables)
    player_object = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        for item in updatables:
            item.update(dt)
        for asteroid in asteroids:
            if asteroid.collision(player_object) == True:
                print("Game over!")
                return
            for shot in shots:
                if shot.collision(asteroid) == True:
                    shot.kill()
                    asteroid.kill()
                
        for item in drawables:
            item.draw(screen)
        pygame.display.flip()
        dt = timeclock.tick(60) / 1000
         
        
    
if __name__ == "__main__":
    main()
