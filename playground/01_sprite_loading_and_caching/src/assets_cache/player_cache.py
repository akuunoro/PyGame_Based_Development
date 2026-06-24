import pygame
from directory_settings import PLAYGROUND_ROOT


sprite_cache = {} #refer to akuunoro_06.08.2026.md - section 1.1

def load_player_sprite(load_filename, load_size=None):
  sprite_settings = (load_filename, load_size) #refer to akuunoro_06.08.2026.md - section 1.2

  if sprite_settings not in sprite_cache:

    sprite = pygame.image.load(
      f"{PLAYGROUND_ROOT}/assets/sprites/players/{load_filename}" #refer to akuunoro_06.08.2026.md - section 1.3
    ).convert_alpha()

    if load_size: #refer to akuunoro_06.08.2026.md - section 1.5
      sprite = pygame.transform.scale(
        sprite, load_size
      )
    
    sprite_cache[sprite_settings] = sprite #refer to akuunoro_06.08.2026.md - section 1.6

  return sprite_cache[sprite_settings]