from src.animations.player_animations import start_idle_animation

class Player:
  def __init__(self): #initialize

    self.frames = start_idle_animation() #refer to akuunoro_06.18.2026.md - section 2.1

    self.frame_index = 0  #refer to akuunoro_06.18.2026.md - section 2.2
    self.animation_speed = 0.15 #refer to akuunoro_06.18.2026.md - section 2.3

    self.x = 50 #position in x (diagonally)
    self.y = 0 #position in y (horizontally)

  def update(self): #update

    self.frame_index += self.animation_speed #refer to akuunoro_06.18.2026.md - section 2.4

    if self.frame_index >= len(self.frames): #refer to akuunoro_06.18.2026.md - section 2.5
        self.frame_index = 0
  
  def draw(self, screen):  #refer to akuunoro_06.18.2026.md - section 2.6

    screen.blit(
        self.frames[int(self.frame_index)], #
        (self.x, self.y)
    )