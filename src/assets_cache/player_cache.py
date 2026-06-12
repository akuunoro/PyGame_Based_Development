import pygame

player_sprite = {}

def load_player_sprite(load_player):
  if load_player not in player_sprite:
    player_sprite[load_player] = pygame.image.load(
      f"assets/sprites/players/{load_player}"
    ).convert_alpha()

  return player_sprite[load_player]