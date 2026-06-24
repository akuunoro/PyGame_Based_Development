from src.assets_cache.enemypr_cache import load_enemypr_sprite

def start_idle_animation(default_size=(220, 220)): 
  return[                                          
    load_enemypr_sprite("Phishing_Rouge1.png", default_size),
    load_enemypr_sprite("Phishing_Rouge2.png", default_size),
    load_enemypr_sprite("Phishing_Rouge3.png", default_size),
    load_enemypr_sprite("Phishing_Rouge4.png", default_size),
    load_enemypr_sprite("Phishing_Rouge5.png", default_size),
    load_enemypr_sprite("Phishing_Rouge6.png", default_size),
    load_enemypr_sprite("Phishing_Rouge7.png", default_size),
    load_enemypr_sprite("Phishing_Rouge8.png", default_size),
    load_enemypr_sprite("Phishing_Rouge9.png", default_size),
    load_enemypr_sprite("Phishing_Rouge10.png", default_size),
  ]

