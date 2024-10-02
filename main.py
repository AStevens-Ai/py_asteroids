import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print('Starting asteroids!')
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    
    print(f"dt: {dt}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    gameScore = 0
    

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    field = AsteroidField()
    player = Player(x, y)
    updatable.add(field)
    updatable.add(player)
    drawable.add(player)
    updatable.add(shots)
    drawable.add(shots)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        delta = clock.tick(60)
        dt = delta / 1000
        
        for update in updatable:
            update.update(dt)
        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game over!")
                return
        for asteroid in asteroids:
            for bullet in shots:
                if bullet.collision(asteroid):
                    gameScore += 1
                    bullet.kill()
                    asteroid.split()
                    
        

        for draw in drawable:
            draw.draw(screen)
        print(f"dt: {dt}")
        
        pygame.display.flip()
        screen.fill('black')

        #generate score and print to screen
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {gameScore}", True, (255, 255,255))
        screen.blit(score_text, (10, 10))

    


if __name__ == "__main__":
    main()