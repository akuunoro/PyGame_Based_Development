from animations.player_animations import start_idle_animation

class Player:
  def __init__(self):

    self.frames = start_idle_animation()

    self.frame_index = 0
    self.animation_speed = 0.15

    self.x = 100
    self.y = 100

  def update(self):

    self.frame_index += self.animation_speed

    if self.frame_index >= len(self.frames):
        self.frame_index = 0
  
  def draw(self, screen):

    screen.blit(
        self.frames[int(self.frame_index)],
        (self.x, self.y)
    )