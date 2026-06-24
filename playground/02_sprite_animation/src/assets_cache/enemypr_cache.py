import pygame
from utils.directory_settings import PLAYGROUND_ROOT


sprite_cache = {} 

def load_enemypr_sprite(load_filename, load_size=None):
  sprite_settings = (load_filename, load_size) 

  if sprite_settings not in sprite_cache:

    sprite = pygame.image.load(
      f"{PLAYGROUND_ROOT}/assets/sprites/enemies/phishing_rouge/{load_filename}" 
    ).convert_alpha()

    if load_size:
      sprite = pygame.transform.scale(
        sprite, load_size
      )
    
    sprite_cache[sprite_settings] = sprite 

  return sprite_cache[sprite_settings]