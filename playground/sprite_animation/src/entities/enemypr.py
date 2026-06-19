from src.animations.enemypr_animations import start_idle_animation

class EnemyPR:
  def __init__(self): #initialize

    self.frames = start_idle_animation() 

    self.frame_index = 0  
    self.animation_speed = 0.15 

    self.x = 550 #position in x (diagonally)
    self.y = 50 #position in y (horizontally)

  def update(self): #update

    self.frame_index += self.animation_speed 

    if self.frame_index >= len(self.frames):
        self.frame_index = 0
  
  def draw(self, screen):  

    screen.blit(
        self.frames[int(self.frame_index)], #
        (self.x, self.y)
    )