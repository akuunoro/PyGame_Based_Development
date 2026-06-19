#akuunoro
import pygame 
from src.entities.player import Player


#SETUP
pygame.init()
screen = pygame.display.set_mode((1280, 720))

pygame.display.set_caption("Playground: Sprite Animation")

#LOAD ASSETS
player = Player()

#GAMEPLAY LOOP
running = True

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  screen.fill((195, 177, 225))
  clock = pygame.time.Clock()

  #RENDER 

  #game data
  player.update()

  #show it
  player.draw(screen)



  pygame.display.flip()
  clock.tick(60)

pygame.quit()