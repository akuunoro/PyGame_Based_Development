#akuunoro
import pygame
from src.entities.player import Player





#SETUP
pygame.init()
clock = pygame.time.Clock()

#SCREEN DISPLAY
screen_wiidth = 1420
screen_height = 720
screen = pygame.display.set_mode((screen_wiidth,screen_height))

pygame.display.set_caption("Playground: Sprite Movement")

#LOAD ASSETS
#player
player = Player()

#enemy



#GAMEPLAY LOOP
running = True

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  screen.fill((195, 177, 225))
  

  #RENDER

  #GAME DATA UPDATE
  player.update()





  #DRAW TO SCREEN
  player.draw(screen)

  pygame.display.flip()
  clock.tick(60)

pygame.quit()