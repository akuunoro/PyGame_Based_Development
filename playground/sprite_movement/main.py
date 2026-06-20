#akuunoro
import pygame



#SETUP
pygame.init()
screen = pygame.display.set_mode((1280,720))

pygame.display.set_caption("Playground: Sprite Movement")

#LOAD ASSETS
#player


#enemy



#GAMEPLAY LOOP
running = True

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  screen.fill((195, 177, 225))
  clock = pygame.time.Clock()

  #RENDER

  #GAME DATA UPDATE




  pygame.display.flip()
  clock.tick(60)

pygame.quit()