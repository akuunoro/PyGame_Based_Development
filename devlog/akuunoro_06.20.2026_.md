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
This specific section talks about how the state update from *'idle'* to *'walking'*, vice versa, are handled. This one is pretty easy. Basically, when we are animating are frames through the list index or frame index, we are iterating through the length of our idle animation. Once we changed state from *'walking'* to *'idle'*, we need a way to reset this frame index. I will explain this in a subsequent nested sections.

##### Section 2.1 
State change when moving (WASD) and Idle. We need to have a way to change our state between *'idle'* and *'walk'* - in this case, storing them or setting them to a variable - as this will be used later on for state checks for syncing the animation frames to specific actions (i.e, idle and walk). 

##### Section 2.2
reset the index to 0 when changing state from idle and walking, vice versa. 

This is achieved by checking the variable *'set_new_state'* from 2.1 against *'self.state'* that is set to *'idle'* in default. Every time we change state, we are going to check if *'set_new_state'*, the new state is not equal (**!=**) to the previous state. Which will be true if it do change a state, we are going to reset our frame index to 0, since we will start to animate the animation frames of the new state now. **THIS IS THE MOST IMPORTANT PART OF THE ENTIRE SPRITE ANIMATION SYNCING** as without this, everything will jsut return an error due to frame index mismatch. **REMEMBER:** **Not every animation will be created to have the same number of frames, that's why this logic is vital.**

In addition, we are initializing the new state stored in *'set_new_state'* to the *'self.state'* to overwrite the old or previous state set in it. 

##### Section 2.3 
check for state change and set the animation frames. This part have a default animation frames used being the idle animation **(*'idle_frames'*)**. This checks the newly updated state of *'self.state'* from **Section 2.2** and assign an approapriate animation frames being *'idle_frames'* and *'walk_frames'* for now. 

##### Section 2.3 
checks for the current state that the player is in, then assign the animation frame to draw. You might notice that this feels redundant as we are checking again just like from **Section 2.3**. I am currently thinking of a way to improve this logic. Bare with me huhu


### UPDATE
I almost forgot to update the Devlog #4. I'm so sorry!!