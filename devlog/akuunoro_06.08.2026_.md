# DEVLOG #1

## June 08, 2026

### Learning PyGame

This is the first commit. I'm currently familiarizing myself with how Pygame file structure works and how Pygame works in general. The most interesting part for me so far is that Pygame runs mostly on your CPU and how the display works specifically the fill and flip methods works, they use a front and back buffer to produce display updates every loop. Pretty interesting tbh. 

### SECTIONS

#### Section 1 - Looping and Get Events
The looping and get event section is the main pygame loop track of running the pygame engine and putting every inputs into the queue for reactive feedback to the buffer of the flip method in Section 3

##### Section 1.1
initialize running to TRUE for game loop

##### Section 1.2
this gets every events or inputs and put it in a queue to be act upon

##### Section 1.3
click x and close, basically a quit event

##### Section 1.4
#stops the game on the next loop check

#### Section 2
can be pygame color set or rgb values by implementing a tuple

#### Section 3
Basically this one, what it does is update the screen using a buffer (front and back). 
The front buffer is the screen that is display and can be seen by the player, while the back buffer is the one that creates or draw the update. Once the pyGame or back buffer is done, it will be sent to the front buffer so it can be shown. 

#### Section 4
Just like closing a db connection or scanner in java using 'close()'. This one use 'quit()' to completely close the pygame engine

#### Section 5
I've tried implementing draw methods in calling the player sprite from image.load method but it does not support the draw attribute. The 'blit' method works as instead of drawing an already created image using the back buffer of the flip method, it will just tell the back buffer to copy the called or set image onto the screen.