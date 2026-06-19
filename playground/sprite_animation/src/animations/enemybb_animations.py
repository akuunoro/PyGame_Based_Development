from src.assets_cache.enemybb_cache import load_enemybb_sprite

def start_idle_animation(default_size=(256, 256)): 
  return[                                          
    load_enemybb_sprite("Backdoor_Bandit1.png", default_size),
    load_enemybb_sprite("Backdoor_Bandit2.png", default_size),
    load_enemybb_sprite("Backdoor_Bandit3.png", default_size),
    load_enemybb_sprite("Backdoor_Bandit4.png", default_size),
    load_enemybb_sprite("Backdoor_Bandit5.png", default_size),
    load_enemybb_sprite("Backdoor_Bandit6.png", default_size),
    load_enemybb_sprite("Backdoor_Bandit7.png", default_size),
    load_enemybb_sprite("Backdoor_Bandit8.png", default_size),
    load_enemybb_sprite("Backdoor_Bandit9.png", default_size),
    load_enemybb_sprite("Backdoor_Bandit10.png", default_size),
  ]

