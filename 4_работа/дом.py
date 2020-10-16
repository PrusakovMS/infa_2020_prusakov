import pygame

pygame.init()

FPS = 30
screen = pygame.display.set_mode((900, 900))

white = (255, 255, 255)
screen.fill(white)


def the_main_part(x, y, i, j, k, height, width):
    # brown = (40, 34, 11)
    pygame.draw.rect(screen, (i, j, k), [x, y - height, width, height])


def lower_windows(x, y, height, width):
    pygame.draw.rect(screen, (200, 200, 200), [x + width / 7, y - 3*height / 11, width / 7, 2*height / 11])
    pygame.draw.rect(screen, (200, 200, 200), [x + 3*width / 7, y - 3*height / 11, width / 7, 2*height / 11])
    pygame.draw.rect(screen, (200, 200, 200), [x + 5*width / 7, y - 3*height / 11, width / 7, 2*height / 11])


def roof(x, y, i, j, k, width, height):
    pygame.draw.polygon(screen, (i, j, k), [(x - width / 7, y - height), (x, y - 12*height / 11),
                                            (x + width, y - 12*height / 11), (x + width / 7, y - height)])






the_main_part(200, 400, 0, 0, 0, 330, 210)
lower_windows(200, 400, 330, 210)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()