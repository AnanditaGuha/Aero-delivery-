import pygame

pygame.init()

display_width = 1080
display_height = 720

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Too Racey')

black = (0, 0, 0)
white = (255, 255, 255)

clock = pygame.time.Clock()
crashed = False
dronImg = pygame.image.load('drone.jpg')


def dron(x, y):
    gameDisplay.blit(dronImg, (x, y))


x = (display_width * 0.45)
y = (display_height * 0.1)

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