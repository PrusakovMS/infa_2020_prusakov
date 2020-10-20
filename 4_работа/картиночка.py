import pygame
from random import randint

pygame.init()

FPS = 30
screen = pygame.display.set_mode((642, 943))

white = (255, 255, 255)
black = (0, 0, 0)
gray = (42, 42, 42)
marroon = (43, 17, 0)
brown = (40, 34, 11)
light_gray = (82, 70, 63)
moon_glow = (235, 245, 255)
yellow = (212, 170, 0)
fon = (102, 102, 102)
krysha = (30, 30, 30)
COLORS = [marroon, yellow]

screen.fill(fon)

# луна и земля
pygame.draw.circle(screen, moon_glow, [577, 83], 55)
pygame.draw.rect(screen, black, [0, 395, 642, 548])

# дома
otstup_zabora = 40
otstup_okna = 41


def house(x, y):
    '''
    Функция house добавляет дом:
    x, y - координаты левого нижнего угла дома
    '''
    # строение
    pygame.draw.rect(screen, brown, [x, y - 244, 171, 244])
    # окна
    pygame.draw.rect(screen, COLORS[randint(0, 1)], [x + 19, y - 63, 33, 41])
    pygame.draw.rect(screen, COLORS[randint(0, 1)], [x + 70, y - 63, 33, 41])
    pygame.draw.rect(screen, COLORS[randint(0, 1)], [x + 121, y - 63, 33, 41])
    # высокие окна
    pygame.draw.rect(screen, light_gray, [x + 32, y - 240, 20, 92])
    pygame.draw.rect(screen, light_gray, [x + 32 + otstup_okna, y - 240, 20, 92])
    pygame.draw.rect(screen, light_gray, [x + 32 + 2 * otstup_okna, y - 240, 20, 92])
    # забор
    pygame.draw.rect(screen, gray, [x - 15, y - 148, 204, 25])
    pygame.draw.rect(screen, gray, [x - 8, y - 181, 186, 10])
    pygame.draw.rect(screen, gray, [x + 17, y - 172, 11, 24])
    pygame.draw.rect(screen, gray, [x + 17 + otstup_zabora, y - 172, 11, 24])
    pygame.draw.rect(screen, gray, [x + 17 + 2 * otstup_zabora, y - 172, 11, 24])
    pygame.draw.rect(screen, gray, [x + 17 + 3 * otstup_zabora, y - 172, 11, 24])
    # крыша
    pygame.draw.polygon(screen, krysha, [[x - 15, y - 245], [x + 9, y - 263], [x + 158, y - 263], [x + 186, y - 245]])
    # трубы
    pygame.draw.rect(screen, gray, [x + 34, y - 305, 12, 54])
    pygame.draw.rect(screen, gray, [x + 101, y - 285, 6, 22])
    pygame.draw.rect(screen, gray, [x + 144, y - 287, 6, 36])
    pygame.draw.rect(screen, gray, [x + 24, y - 288, 6, 36])


# облачки
surface = pygame.Surface([642, 943], pygame.SRCALPHA, 32)
surface = surface.convert_alpha()
pygame.draw.ellipse(screen, (77, 77, 77), (29, 88, 340, 80))
pygame.draw.ellipse(screen, (51, 51, 51), (281, 61, 320, 80))
pygame.draw.ellipse(screen, (77, 77, 77), [381, 140, 290, 70])
pygame.draw.ellipse(surface, (0, 0, 0, 50), (280, 193, 360, 60))
pygame.draw.ellipse(surface, (52, 52, 52, 100), (114, 360, 440, 60))
pygame.draw.ellipse(surface, (52, 52, 52, 100), (282, 438, 440, 60))
pygame.draw.ellipse(surface, (52, 52, 52, 100), (0, 500, 300, 80))

# призраки
'''
Функции ghostr и ghostl добавляет призраков, повернутых лицом направо
и налево соответственно:
x, y - координаты центра "лица" призрака
r - радиус 
Функции ghostr и ghostl добавляет призраков, повернутых лицом направо
и налево соответственно:
x, y - координаты центра "лица" призрака
r - радиус "лица" призрака
i, j, k - цвет призрака
p - мера его прозрачности
'''
def ghostl(i, j, k, p):
    x = randint(100, 500)
    y = randint(100, 800)
    r = randint(30, 50)
    pygame.draw.circle(surface, (i, j, k, p), (x, y), r)
    pygame.draw.rect(surface, (i, j, k, p), (x - r, y, 2 * r, 1.3 * r))
    pygame.draw.polygon(surface, (i, j, k, p),
                        [(x - r, y + 1.3 * r), (x - r, y + 1.6 * r), (x - r + 0.33 * r, y + 1.4 * r),
                         (x - r + 2 * 0.33 * r, y + 1.6 * r), (x - r + 3 * 0.33 * r, y + 1.4 * r),
                         (x - r + 4 * 0.33 * r, y + 1.6 * r), (x - r + 5 * 0.33 * r, y + 1.4 * r),
                         (x + r, y + 1.6 * r), (x + r, y + 1.3 * r)])
    pygame.draw.circle(surface, (225, 225, 225, 225), [x - int(0.5 * r), y - int(0.5 * r)], int(0.3 * r))
    pygame.draw.circle(surface, (0, 0, 0 / 225), [x - int(0.5 * r), y - int(0.5 * r)], int(0.1 * r))
    pygame.draw.circle(surface, (225, 225, 225, 225), [x + int(0.25 * r), y - int(0.25 * r)], int(0.3 * r))
    pygame.draw.circle(surface, (0, 0, 0, 225), [x + int(0.25 * r), y - int(0.25 * r)], int(0.1 * r))


def ghostr(i, j, k, p):
    x = randint(100, 500)
    y = randint(100, 800)
    r = randint(30, 50)
    pygame.draw.circle(surface, (i, j, k, p), (x, y), r)
    pygame.draw.rect(surface, (i, j, k, p), (x - r, y, 2 * r, 1.3 * r))
    pygame.draw.polygon(surface, (i, j, k, p),
                        [(x - r, y + 1.3 * r), (x - r, y + 1.6 * r), (x - r + 0.33 * r, y + 1.4 * r),
                         (x - r + 2 * 0.33 * r, y + 1.6 * r), (x - r + 3 * 0.33 * r, y + 1.4 * r),
                         (x - r + 4 * 0.33 * r, y + 1.6 * r), (x - r + 5 * 0.33 * r, y + 1.4 * r),
                         (x + r, y + 1.6 * r), (x + r, y + 1.3 * r)])
    pygame.draw.circle(surface, (225, 225, 225, 225), [x - int(0.25 * r), y - int(0.25 * r)], int(0.3 * r))
    pygame.draw.circle(surface, (0, 0, 0, 225), [x - int(0.25 * r), y - int(0.25 * r)], int(0.1 * r))
    pygame.draw.circle(surface, (225, 225, 225, 225), [x + int(0.5 * r), y - int(0.5 * r)], int(0.3 * r))
    pygame.draw.circle(surface, (0, 0, 0, 225), [x + int(0.5 * r), y - int(0.5 * r)], int(0.1 * r))


# рисуем наконец
house(220, 594)
house(15, 688)
house(467, 469)
# red = ((255,0,0))
# orange = ((255,100,10))
# blue = ((0,0,255))
# pink = ((255,100,180))
ghostl(255, 0, 0, 250)
ghostr(255, 100, 180, 120)
ghostr(0, 0, 255, 100)
ghostl(255, 100, 10, 150)
screen.blit(surface, (0, 0))
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()


def ghostl(x, y, r, i, j, k, p):
    pygame.draw.circle(surface, (i, j, k, p), (x, y), r)
    pygame.draw.rect(surface, (i, j, k, p), (x - r, y, 2 * r, 1.3 * r))
    pygame.draw.polygon(surface, (i, j, k, p),
                        [(x - r, y + 1.3 * r), (x - r, y + 1.6 * r), (x - r + 0.33 * r, y + 1.4 * r),
                         (x - r + 2 * 0.33 * r, y + 1.6 * r), (x - r + 3 * 0.33 * r, y + 1.4 * r),
                         (x - r + 4 * 0.33 * r, y + 1.6 * r), (x - r + 5 * 0.33 * r, y + 1.4 * r),
                         (x + r, y + 1.6 * r), (x + r, y + 1.3 * r)])
    pygame.draw.circle(screen, (225, 225, 225), [x - int(0.5 * r), y - int(0.5 * r)], int(0.3 * r))
    pygame.draw.circle(screen, (0, 0, 0), [x - int(0.5 * r), y - int(0.5 * r)], int(0.1 * r))
    pygame.draw.circle(screen, (225, 225, 225), [x + int(0.25 * r), y - int(0.25 * r)], int(0.3 * r))
    pygame.draw.circle(screen, (0, 0, 0), [x + int(0.25 * r), y - int(0.25 * r)], int(0.1 * r))


def ghostr(x, y, r, i, j, k, p):
    pygame.draw.circle(surface, (i, j, k, p), (x, y), r)
    pygame.draw.rect(surface, (i, j, k, p), (x - r, y, 2 * r, 1.3 * r))
    pygame.draw.polygon(surface, (i, j, k, p),
                        [(x - r, y + 1.3 * r), (x - r, y + 1.6 * r), (x - r + 0.33 * r, y + 1.4 * r),
                         (x - r + 2 * 0.33 * r, y + 1.6 * r), (x - r + 3 * 0.33 * r, y + 1.4 * r),
                         (x - r + 4 * 0.33 * r, y + 1.6 * r), (x - r + 5 * 0.33 * r, y + 1.4 * r),
                         (x + r, y + 1.6 * r), (x + r, y + 1.3 * r)])
    pygame.draw.circle(screen, (225, 225, 225), [x - int(0.25 * r), y - int(0.25 * r)], int(0.3 * r))
    pygame.draw.circle(screen, (0, 0, 0), [x - int(0.25 * r), y - int(0.25 * r)], int(0.1 * r))
    pygame.draw.circle(screen, (225, 225, 225), [x + int(0.5 * r), y - int(0.5 * r)], int(0.3 * r))
    pygame.draw.circle(screen, (0, 0, 0), [x + int(0.5 * r), y - int(0.5 * r)], int(0.1 * r))


# рисуем наконец
house(220, 594)
house(15, 688)
house(467, 469)
# red = ((255,0,0))
# orange = ((255,100,10))
# blue = ((0,0,255))
# pink = ((255,100,180))
ghostl(508, 699, 50, 255, 0, 0, 250)
ghostr(134, 746, 30, 255, 100, 180, 120)
ghostr(107, 791, 30, 0, 0, 255, 100)
ghostl(519, 543, 40, 255, 100, 10, 150)
screen.blit(surface, (0, 0))
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
