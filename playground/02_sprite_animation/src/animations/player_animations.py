from src.assets_cache.player_cache import load_player_sprite

def start_idle_animation(default_size=(256, 256)): # refer to akuunoro_06.18.2026.md - section 1.1
  return[                                          # refer to akuunoro_06.18.2026.md - section 1.2
    load_player_sprite("Knight Idle 1.png", default_size),
    load_player_sprite("Knight Idle 2.png", default_size),
    load_player_sprite("Knight Idle 3.png", default_size),
    load_player_sprite("Knight Idle 4.png", default_size),
    load_player_sprite("Knight Idle 5.png", default_size),
    load_player_sprite("Knight Idle 6.png", default_size),
    load_player_sprite("Knight Idle 7.png", default_size),
    load_player_sprite("Knight Idle 8.png", default_size),
    load_player_sprite("Knight Idle 9.png", default_size),
    load_player_sprite("Knight Idle 10.png", default_size),
  ]

