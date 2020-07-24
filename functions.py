import pygame
from parameters import *


def draw_background(display):
    for i in range(20, 220, 20):
        pygame.draw.line(display, dark_gray, (i, 20), (i, 200), 1)
        pygame.draw.line(display, dark_gray, (20, i), (200, i), 1)


def draw_square(row, col, display):
    (x, y) = rowcol2xy(row, col)
    pygame.draw.line(display, white, (x-9, y-9), (x+9, y-9), 3)
    pygame.draw.line(display, white, (x-9, y-9), (x-9, y+9), 3)
    pygame.draw.line(display, dark_gray, (x+9, y+9), (x-9, y+9), 3)
    pygame.draw.line(display, dark_gray, (x+9, y+9), (x+9, y-9), 3)
    pygame.draw.rect(display, gray, (x-7, y-7, 14, 14), 0)


mine_pic = pygame.transform.scale(pygame.image.load('mine.jpg'), (20, 20))
exploded_mine_pic = pygame.transform.scale(pygame.image.load('exploded.jpg'), (20, 20))
flag_pic = pygame.transform.scale(pygame.image.load('flag.png'), (15, 15))


def draw_mine(display, row, col):
    (x, y) = rowcol2xy(row, col)
    display.blit(mine_pic, (x-10, y-10), special_flags=4)


def draw_exploded_mine(display, row, col):
    (x, y) = rowcol2xy(row, col)
    display.blit(exploded_mine_pic, (x-10, y-10))


def draw_flag(display, row, col):
    (x, y) = rowcol2xy(row, col)
    display.blit(flag_pic, (x-8, y-8), special_flags=4)


def rowcol2xy(row, col):
    x = 30 + (col*20)
    y = 30 + (row*20)
    return x, y


def xy2rowcol(x, y):
    if (20 <= x <= 200) and (20 <= y <= 200):
        row = (y-20) // 20
        col = (x-20) // 20
        return row, col
    else:
        return -1, -1


def number2color(number):
    switcher = {1: blue, 2: green, 3: red, 4: navy, 5: dark_red, 6: teal, 7: black, 8: gray_for8}
    return switcher.get(number, "not a defined color")


def number2screen(number, display, row, col):
    x, y = rowcol2xy(row, col)
    color = number2color(number)
    font = pygame.font.SysFont(None, 25)
    screen_text = font.render(str(number), True, color)
    display.blit(screen_text, [x-4, y-7])


def text2screen(text, display, color, size, x, y):
    font = pygame.font.SysFont(None, size)
    screen_text = font.render(text, True, color)
    display.blit(screen_text, [x, y])

