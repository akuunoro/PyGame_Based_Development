# DEVLOG #3

## June 18, 2026

### Learning How PyGame Works
Today, I will start exploring how sprite animation works. I will just limit it to one concept for now.

### SECTIONS
#### Section 1 - Player Animation
This is such an easy task, basically we can just call our cached images from 'player_cache' then just load our frames for an idle animation. Thereafter, just set our desired size.

##### Section 1.1
we are just calling our cache images or sprite (if it is already cached), then load it frame by frame in sequential manner to have an animation

##### Section 1.2
all of this animations are stored in a list

#### Section 2 - Initialize, Update and Draw
so I can create a class that i can call in our 'main.py' that will initialize, update the frames 

##### Section 2.1 
use the animation's frame of the images

##### Section 2.2 
start with the first frame or image

##### Section 2.3
the speed of how do we interate through the frames. This makes sure that we won't iterate quickly through frames creating a wonky speedy animation

##### Section 2.4
updates everything for our animation, in our case for 0, 0.15, 0.30, 0.45, 0.60, 0.75, 0.90, 1.05

##### Section 2.5
if the frame_index (the int one) reaches the maximum frame, in our case, the 10nth frame (10nth index)

##### Section 2.6
this is where we use the blit now, instead in the main.py. From before, we are calling the cached image. Now, the frame or each image in the iteration then set the position, which is here too.

##### Section 2.7
the int basically handles or correct the floating values from updates as list indices only takes integers as its values, not '0.15'

### UPDATE
Finished this topic today, June 20, 2026. What an interesting way of implementing sprite animation and I love how it ties back to loading and caching of sprites (images). I might linger here for a bit as I want to try how's the memory management or budgeting