import pygame

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

white = ((255,255,255))
red = ((255,0,0))
yellow = ((255,255,0))
black = ((0,0,0))

screen.fill(white)

pygame.draw.circle(screen, yellow, [200, 200], 200)
pygame.draw.circle(screen, red, [120, 150], 50)
pygame.draw.circle(screen, black, [120, 150], 25)
pygame.draw.circle(screen, red, [280, 150], 45)
pygame.draw.circle(screen, black, [280, 150], 20)
pygame.draw.rect(screen, black, [80, 300, 225, 50])
pygame.draw.polygon(screen, black, [[150, 120], [160, 110], [30, 20], [20, 30]])
pygame.draw.polygon(screen, black, [[240, 130], [230,120], [380, 30], [390, 40]])

#wasd



pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()