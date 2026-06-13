import pygame
from directory_settings import PLAYGROUND_ROOT


sprite_cache = {} #dictionary to store the sprites that we will cache

def load_player_sprite(load_filename, load_size=None):
  sprite_settings = (load_filename, load_size)  #this will act as a key for the dictionary, while its contents inside will be the value of this key

  if sprite_settings not in sprite_cache:

    sprite = pygame.image.load(
      f"{PLAYGROUND_ROOT}/assets/sprites/players/{load_filename}" #apparently, the pygame still works in the parent directory. So i need to backtrack to it.
    ).convert_alpha()

    if load_size: #wether there's a size set or not, if there's not. Ignore this.
      sprite = pygame.transform.scale(
        sprite, load_size
      )
    
    sprite_cache[sprite_settings] = sprite #set it in the dictionary

  return sprite_cache[sprite_settings]