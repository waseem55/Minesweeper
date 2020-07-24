#--------------------------------------------------------------------------------
#Author: Waseem Orphali 
#Create Date: 06/15/2019
#Project Name: Minesweeper
#Description: 
#An attempted replica of the old Windows minesweeper.
#The game is made using Pygame library
#https://www.pygame.org/docs/
#Currently, the game only supports 9*9 grid with 10 mines. Future plan is to support varying sizes and number of mines.
#
#--------------------------------------------------------------------------------

import pygame
from parameters import *
from functions import *
from game_class import Minesweeper
import time

pygame.init()


game_display = pygame.display.set_mode((display_w, display_h))
game_display.fill(gray)
pygame.display.set_caption("Minesweeper")
game = Minesweeper(game_display)
#game.init_mines(1, 1)

draw_background(game_display)
game.draw_new_game()
first_click = True
running = True
lost = False
won = False
while running:
    game_display.fill(gray)
    text2screen("press n for new game", game_display, blue, 25, 25, 0)
    draw_background(game_display)
    game.draw_numbers()
    game.draw_squares(lost)
    game.draw_flags()

    remaining_squares = sum(x.count(0) for x in game.clicked)
    if remaining_squares == 10 and not lost:
        won = True

    if won:
        text2screen("You Won!", game_display, green, 30, 60, 203)
    if lost:
        draw_exploded_mine(game_display, rowup, colup)
        text2screen("You Suck!", game_display, red, 35, 50, 200)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_n:
            game.init_game(1, 1)
            game.draw_new_game()
            first_click = True
            lost = False
            won = False

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3 and not (lost or won):
            (xleft, yleft) = pygame.mouse.get_pos()
            game.set_flag(xleft, yleft)
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not (lost or won):
            (x, y) = pygame.mouse.get_pos()
            (rowdown, coldown) = xy2rowcol(x, y)
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1 and not (lost or won):
            (x, y) = pygame.mouse.get_pos()
            (rowup, colup) = xy2rowcol(x, y)
            if rowdown == rowup and coldown == colup and game.flags[rowup][colup] != 1:
                if first_click:
                    game.init_game(rowup, colup)
                    first_click = False
                lost = game.click_square(rowup, colup)

    pygame.display.update()


pygame.quit()
quit()




