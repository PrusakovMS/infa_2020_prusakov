import pygame

pygame.init()

FPS = 30
screen = pygame.display.set_mode((500, 600))

white = (255, 255, 255)
black = (0, 0, 0)
gray = (180, 180, 180)
marroon = (43, 17, 0)
blue = (255, 0, 0)
pink = ((255,100,180))

screen.fill(white)


def draw_body(x, y, width, height, colour):
    '''
    Функция рисует тело зайца
    x, y - координаты центра изображения
    width, height - ширина и высота изобажения
    colour - цвет, заданный в формате, подходящем для pygame.Color
    '''
    pygame.draw.ellipse(screen, colour, (x - width // 2, y - height // 2, width, height))

def draw_belly(x, y, width, height, colour):
    '''
    Функция рисует тело зайца
    x, y - координаты центра изображения
    width, height - ширина и высота изобажения
    colour - цвет, заданный в формате, подходящем для pygame.Color
    '''
    pygame.draw.ellipse(screen, colour, (x - width // 2, y - height // 2, width, height))


def draw_head(x, y, size, colour):
    '''
    Функция рисует голову зайца.
    x, y - координаты центра изображения
    size - диаметр головы
    colour - цвет, заданный в формате, подходящем для pygame.Color
    '''
    pygame.draw.circle(screen, colour, (x, y), size // 2)


def draw_eye(x, y, size, colour):
    '''
    Функция рисует глаза зайца.
    x, y - координаты центра изображения
    size - диаметр глаза
    colour - цвет, заданный в формате, подходящем для pygame.Color
    '''
    pygame.draw.circle(screen, colour, (x, y), size // 2)
    pygame.draw.circle(screen, black, (x, y), size // 3)

def draw_mouth(x, y, width, height, colour):
    '''
    Функция рисует рот зайца.
    x, y - координаты левого верхнего угла изображения
    width, height - ширина и высота изобажения
    colour - цвет, заданный в формате, подходящем для pygame.Color
    '''
    pi = 3.14
    pygame.draw.arc(screen, colour, (x, y, width, height), pi, 2*pi)


def draw_nose(x, y, size):
    '''
    Функция рисует нос зайца.
    x, y - координаты носа
    size - диаметр носа
    colour - цвет, заданный в формате, подходящем для pygame.Color
    '''
    pygame.draw.circle(screen, pink, (x, y), size)

def draw_leg(x, y, width, height, colour):
    '''
    Функция рисует ногу зайца.
    x, y - координаты центра изображения
    width, height - ширина и высота изобажения
    colour - цвет, заданный в формате, подходящем для pygame.Color
    '''
    pygame.draw.ellipse(screen, colour, (x - width // 2, y - height // 2, width, height))


def draw_ear(x, y, width, height, colour):
    '''
    Функция рисует ухо зайца.
    x, y - координаты центра изображения
    width, height - ширина и высота изобажения
    colour - цвет, заданный в формате, подходящем для pygame.Color
    '''
    pygame.draw.ellipse(screen, colour, (x - width // 2, y - height // 2, width, height))

def draw_hare(x, y, width, height, colour):
    '''
    Функция рисует зайца на экране.
    x, y - координаты центра изображения
    width, height - ширина и высота изобажения
    colour - цвет, заданный в формате, подходящем для pygame.Color
    '''
    body_width = width // 2
    body_height = height // 2
    body_y = y + body_height // 2
    draw_body(x, body_y, body_width, body_height, colour)

    draw_belly(x, body_y, body_width // 1.5, body_height // 1.5, (150, 150, 150))

    head_size = height // 4
    draw_head(x, y - head_size // 2, head_size, colour)

    ear_height = height // 3
    ear_y = y - height // 2 + ear_height // 2
    for ear_x in (x - head_size // 4, x + head_size // 4):
        draw_ear(ear_x, ear_y, width // 8, ear_height, colour)

    draw_eye(x - head_size // 4, y - 3 * head_size // 4, head_size // 4, (0, 0, 255))
    draw_eye(x + head_size // 4, y - 3 * head_size // 4, head_size // 4, (0, 0, 255))

    draw_nose(x + head_size // 30, y - head_size // 2, head_size // 30)

    draw_mouth(x-head_size // 3.5, y - head_size // 1.9, head_size // 3, head_size // 3, (255, 255, 255))
    draw_mouth(x+head_size // 25, y - head_size // 1.9, head_size // 3, head_size // 3, (255, 255, 255))

    leg_height = height // 16
    leg_y = y + height // 2 - leg_height // 2
    for leg_x in (x - width // 4, x + width // 4):
        draw_leg(leg_x, leg_y, width // 4, leg_height, colour)


draw_hare(250, 250, 250, 400, (100, 100, 100))


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
