import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

             
def main():
    print("Starting asteroids!")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()

    Shot.containers = (shots, updatable, drawable)

    while True:
        # Game loop
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
            for obj in updatable:
                obj.update(dt)
            
            screen.fill('black')

            for obj in drawable:
                obj.draw(screen)

            for asteroid in asteroids:  
                player_collision = asteroid.check_for_collision(player)
                if player_collision:
                    print("Game over!")
                    exit()
                
                for shot in shots:
                    shot_collision = asteroid.check_for_collision(shot )
                    if shot_collision:
                        asteroid.split() 
                        shot.kill()
                
            pygame.display.flip()

            dt = clock.tick(60) / 1000 
    
    pygame.quit()



if __name__ == "__main__":
    main()
