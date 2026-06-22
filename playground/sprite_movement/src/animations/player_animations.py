from src.assets_cache.player_cache import load_player_sprite


def start_idle_animation(default_size = (256,256)):
  return[
    load_player_sprite("idle/Knight_Idle1.png", default_size),
    load_player_sprite("idle/Knight_Idle2.png", default_size),
    load_player_sprite("idle/Knight_Idle3.png", default_size),
    load_player_sprite("idle/Knight_Idle4.png", default_size),
    load_player_sprite("idle/Knight_Idle5.png", default_size),
    load_player_sprite("idle/Knight_Idle6.png", default_size),
    load_player_sprite("idle/Knight_Idle7.png", default_size),
    load_player_sprite("idle/Knight_Idle8.png", default_size),
    load_player_sprite("idle/Knight_Idle9.png", default_size),
    load_player_sprite("idle/Knight_Idle10.png", default_size),

  ]


def start_walking_animation(default_size = (256,256)):
  return [
    load_player_sprite("walk/Knight_Walk1.png", default_size),
    load_player_sprite("walk/Knight_Walk2.png", default_size),
    load_player_sprite("walk/Knight_Walk3.png", default_size),
    load_player_sprite("walk/Knight_Walk4.png", default_size),

  ]

