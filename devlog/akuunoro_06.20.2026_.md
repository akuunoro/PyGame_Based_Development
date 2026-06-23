# DEVLOG #4

## June 20, 2026

### Learning How PyGame Works
Today, I will start exploring how player movement works and how do I implement the walking animation of the sprite alongside their movement. Maybe even border and object collisions if I have more time. 

### SECTIONS
#### Section 1 - Sprite Animation Syncing
In order to sync a sprite with a specific movement. We need to have two different lists iin 'player_animations.py' whereas one is for 'idle' and one is for 'walk'. Refer to our function objects in 'player_animations.py', the 'start_idle_animation' and 'start_walking_animation'

##### Section 1.1
We are initializing two frames: the idle_framess and walk_frames that are both dependent on our current state that I will discuss later on how it will update itself. These two (2) said frames are initialize on their respective animations being the 'start_idle_animation' and 'start_walking_animation'

#### Section 2 - Self State Update and Animation Frame Syncing Reset Loop
This specific section talks about how the state update from 'idle' to 'walking', vice versa, are handled. This one is pretty easy. Basically, when we are animating are frames through the list index or frame index, we are iterating through the length of our idle animation. Once we changed state from 'walking' to 'idle', we need a way to reset this frame index. I will explain this in a subsequent nested sections.

##### Section 2.1 


### UPDATE
