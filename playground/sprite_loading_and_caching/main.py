# akuunoro
import pygame
from src.assets_cache.player_cache import load_player_sprite
from src.assets_cache.enemy_cache import load_enemy_sprite

# SETUP
pygame.init()  # initialize all pygame modules
# tuple for display screen (width,pixel)
screen = pygame.display.set_mode((1280, 720))

pygame.display.set_caption("Test Game by akuunoro")  # setting caption

# LOAD ASSETS
## players
player = load_player_sprite("Knight (Front)1.png", (64, 64))
player2 = load_player_sprite("Knight (Front)1.png", (64, 64))


##enemies
enemy1 = load_enemy_sprite("Backdoor_Bandit1.png", (64,64))
enemy2 = load_enemy_sprite("PhishingRouge1.png", (64,64))

running = True  # refer to akuunoro_06.08.2026.md - section 1.1

# SET GAME LOOP TO RUN
while running:
    for event in pygame.event.get():  # refer to akuunoro_06.08.2026.md - section 1.2
        if event.type == pygame.QUIT:  # refer to akuunoro_06.08.2026.md - section 1.3
            running = False  # refer to akuunoro_06.08.2026.md - section 1.4

    # the bg
    screen.fill((0, 0, 0))  # refer to akuunoro_06.08.2026.md - section 2
    clock = pygame.time.Clock()

    # RENDER GAME
    # refer to akuunoro_06.08.2026.md - section 5
    
    screen.blit(player, (100, 100))
    screen.blit(player, (150, 100))

    screen.blit(enemy1, (150, 167))
    screen.blit(enemy2, (154, 545))



    # idk if this is right, but this is how I understand it
    pygame.display.flip()  # refer to akuunoro_06.08.2026.md - section 3
    clock.tick(60)


pygame.quit()  # refer to akuunoro_06.08.2026.md - section 4
