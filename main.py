#akuunoro
import pygame

# SETUP
pygame.init() #initialize all pygame modules
screen = pygame.display.set_mode((1280, 720)) # tuple for display screen (width,pixel)


pygame.display.set_caption("Test Game by akuunoro") #setting caption

running = True#initialize running to TRUE for game loop

# SET GAME LOOP TO RUN
while running:
    for event in pygame.event.get(): #this gets every events or inputs and put it in a queue to be act upon
        if event.type == pygame.QUIT:  # click x and close, basically a quit event
            running = False #stops the game on the next loop check
    
    #the bg
    screen.fill((0, 0, 0)) #can be pygame color set or rgb values by implementing a tuple

    # RENDER GAME
   
    #idk if thisis right, but this is how I understand it
    pygame.display.flip() #basically this one, what it does is update the screen using a buffer (front and back). 
    """The front buffer is the screen that is display and can be seen by the player, while the back buffer is the one that
    creates or draw the update. Once the pyGame or back buffer is done, it will be sent to the front buffer so it can be shown"""


pygame.quit() #just like closing a db connection or scanner in java using 'close()'. This one use 'quit()' to completely close the pygame engine
