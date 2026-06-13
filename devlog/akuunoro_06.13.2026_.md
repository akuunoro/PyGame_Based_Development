# DEVLOG #2

## June 08, 2026

### Folder Structure Changes and GitHub Comment Title Label Changes
Okay, I've decided to refractor and change the entire folder structure of my repository. Mainly due to me wanting to separate the directories for just pure studying the concepts and logic - being the [Playground](../playground/) directory, and a directory for projects (that will mostly contains mini games, but probably some major games) to apply those concepts and logic I've studied on a real game. 

Thereafter, I've changed the Github Comment Title Label for every commits that I will do. Sorry, I can't really decide a comment title label last June 08, and I just went in and do it without proper planning. But HEY! This time, this will be the permanent commit comment title label (FOR NOW HAHAHA). Refer to [README](../README.md)

### Learning How PyGame Works
Today, I will start exploring how sprite loading, sprite caching, and sprite animation works. Maybe also character movements.


### SECTIONS
#### Section 1 - Sprite Loading and Sprite Caching
Basically in sprite loading, we are using blit so that we can put the image or sprite as it is then we can set its position using a tuple of (x,y). On one hand, in sprite caching, we are utilizing a dictionary, where the dictionary will store the set parameters or settings of our sprite. In our case, i am caching the filename of the sprite and its dimension size. 

##### Section 1.1 
dictionary to store the sprites that we will cache. Basically, both the filename and its custome size (if there is) will be stored here.

##### Section 1.2
this will act as a key for the dictionary, while its contents inside will be the value of this key. Being the filename and size (filename, size)

##### Section 1.3
apparently, the pygame still works in the parent directory. When I run the main.py, it still starts at the root directory so it starts looking from there when i use directory lookup. So i need to backtrack to it using directory_settings.py specifically pathlib (Path(__file__).resolve())

##### Section 1.4
the directory settings so i can back track to the parent or root directory, in order for me to run or call the images or whatever files

##### Section 1.5
wether there's a size set or not, if there's not. Ignore this. 

##### Section 1.6
set it in the dictionary, being {(filename, size): surface}