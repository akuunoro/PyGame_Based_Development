import pygame
from src.animations.player_animations import start_idle_animation, start_walking_animation 

class Player:
  def __init__(self): #initialize

    #refer to akuunoro_06.20.2026.md - section 1.1
    #animation - idle
    self.idle_frames = start_idle_animation() 
    #animation - walking
    self.walk_frames = start_walking_animation()

    #initial animation states
    self.state = "idle"


    self.frame_index = 0  
    self.animation_speed = 0.15 

    self.x = 50 #position in x (diagonally)
    self.y = 0 #position in y (horizontally)

  def update(self): #update
    keys = pygame.key.get_pressed()
    moving = False

    #WASD key press
    if keys[pygame.K_a]:
      self.x -= 5
      moving = True

    if keys[pygame.K_d]:
      self.x += 5
      moving = True

      
    if keys[pygame.K_w]:
      self.y -= 5
      moving = True
  
    if keys[pygame.K_s]:
      self.y += 5
      moving = True

      

    #state change when moving (WASD) and Idle
    if moving:
      set_new_state = "walk" #WTFFFFFFFFFFFFFFFFFFFFF
    else: 
      set_new_state = "idle"

    #reset the index to 0 when changing state from idle and walking, vice versa
    if set_new_state != self.state:
      self.state = set_new_state
      self.frame_index = 0

    state_animation = self.idle_frames
    #check for state change and set the animation frames
    if self.state  == "idle":
      state_animation = self.idle_frames
    elif self.state == "walk":
      state_animation = self.walk_frames
    
    #animation frame update and iteration
    self.frame_index += self.animation_speed 

    if self.frame_index >= len(state_animation):
        self.frame_index = 0
  
  def draw(self, screen):  
    
    current_frames = self.idle_frames
    if self.state  == "idle":
      current_frames = self.idle_frames
    elif self.state == "walk":
      current_frames = self.walk_frames

    screen.blit(
        current_frames[int(self.frame_index)], #
        (self.x, self.y)
    )