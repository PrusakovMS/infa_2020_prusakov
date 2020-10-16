import pygame

pygame.init()

FPS = 30
screen = pygame.display.set_mode((500, 500))

white = (255, 255, 255)
black = (0, 0, 0)
gray = (42, 42, 42)
marroon = (43, 17, 0)
brown = (40, 34, 11)
light_gray = (82, 70, 63)
moon_glow = (235, 245, 255)
yellow = (255,255,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

r = 50
n = 3

screen.fill(white)


def smile1(x, y):
    pygame.draw.circle(screen, yellow, (x, y),  r)
    pygame.draw.circle(screen, red, (x-int(0.5*r), y-int(0.5*r)), int(0.3*r))
    pygame.draw.circle(screen, red, (x + int(0.5 * r), y - int(0.5 * r)), int(0.3 * r))
    pygame.draw.circle(screen, black, (x - int(0.5 * r), y - int(0.5 * r)), int(0.2 * r))
    pygame.draw.circle(screen, black, (x + int(0.5 * r), y - int(0.5 * r)), int(0.2 * r))
    pygame.draw.rect(screen, black, (x-0.65*r, y+0.33*r, 1.3*r, 0.33*r))



def smile2(x, y):
    pygame.draw.circle(screen, green, (x, y), r)
    pygame.draw.circle(screen, blue, (x - int(0.5 * r), y - int(0.5 * r)), int(0.3 * r))
    pygame.draw.circle(screen, blue, (x + int(0.5 * r), y - int(0.5 * r)), int(0.3 * r))
    pygame.draw.circle(screen, black, (x - int(0.5 * r), y - int(0.5 * r)), int(0.2 * r))
    pygame.draw.circle(screen, black, (x + int(0.5 * r), y - int(0.5 * r)), int(0.2 * r))
    pygame.draw.rect(screen, black, (x - 0.65 * r, y + 0.33 * r, 1.3 * r, 0.33 * r))


for i in range(n):
    for j in range(n):
        if (i*n + j) % 2:
            smile2(100 + r * 3 * j, 100 + r * 3 * i)
        else:
            smile1(100 + r * 3 * j, 100 + r * 3 * i)






pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
