from src.animations.player_animations import start_idle_animation, start_walking_animation

class Player:
  def __init__(self): #initialize

    self.frames = start_idle_animation() 

    self.frame_index = 0  
    self.animation_speed = 0.15 

    self.x = 50 #position in x (diagonally)
    self.y = 0 #position in y (horizontally)

  def update(self): #update

    self.frame_index += self.animation_speed 

    if self.frame_index >= len(self.frames):
        self.frame_index = 0
  
  def draw(self, screen):  

    screen.blit(
        self.frames[int(self.frame_index)], #
        (self.x, self.y)
    )