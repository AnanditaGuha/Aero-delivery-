#pygame is a module 
import pygame

#intitialize pygame - turn it on
pygame.init()


display_width = 1080
display_height = 720

#make the window
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Too Racey')

#make some colors (R,G,B)
black = (0, 0, 0)
white = (255, 255, 255)


clock = pygame.time.Clock()
crashed = False

#load image
dronImg = pygame.image.load('drone.jpg')

#function to draw the image
def dron(x, y):
    gameDisplay.blit(dronImg, (x, y))


x = (display_width * 0.45) #set x to the middle 
y = (display_height * 0.1)#set y to bottom

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    gameDisplay.fill(white)
    dron(x, y)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
