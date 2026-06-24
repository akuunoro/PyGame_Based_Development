#akuunoro
import pygame 
from src.entities.player import Player
from src.entities.enemybb import EnemyBB
from src.entities.enemypr import EnemyPR


#SETUP
pygame.init()
screen = pygame.display.set_mode((1280, 720))

pygame.display.set_caption("Playground: Sprite Animation")

#LOAD ASSETS
#player
player = Player()

#enemies
enemybb = EnemyBB()
enemypr = EnemyPR()

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
  #update player
  player.update()

  #update enemy
  enemybb.update()
  enemypr.update()

  #show it
  player.draw(screen)
  enemybb.draw(screen)
  enemypr.draw(screen)

  pygame.display.flip()
  clock.tick(60)

pygame.quit()