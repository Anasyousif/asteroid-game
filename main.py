import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable,drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()
    while True:
        # 1. Calculate time first
        dt = clock.tick(60) / 1000

        # 2. Check for the Quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # 3. Update the player state
        updatable.update(dt)
        log_state()
        # 4. Draw to the screen
        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()           
if __name__ == "__main__":
    main()