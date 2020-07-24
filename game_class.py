import random
import pygame
import numpy as np
from functions import draw_square, number2screen, draw_flag, draw_exploded_mine, draw_mine, xy2rowcol


class Minesweeper:
    def __init__(self, display):
        self.mines = np.zeros((9, 9), dtype=int)
        self.display = display
        self.flags = np.zeros((9, 9), dtype=int)
        self.clicked = np.zeros((9, 9), dtype=int).tolist()
        self.clicked.append([1, 1, 1, 1, 1, 1, 1, 1, 1])
        self.clicked.insert(0, [1, 1, 1, 1, 1, 1, 1, 1, 1])
        for i in range(len(self.clicked)):
            self.clicked[i].insert(0, 1)
            self.clicked[i].append(1)

    def init_game(self, x, y):
        # 9 means there is a mine
        # A bigger list is created to make it easier to count number of mines
        #  around a square without having to deal w edges
        game_list = np.zeros((11, 11), dtype=int)
        self.mines = np.zeros((9, 9), dtype=int)
        self.flags = np.zeros((9, 9), dtype=int)
        self.clicked = np.zeros((9, 9), dtype=int).tolist()
        self.clicked.append([1, 1, 1, 1, 1, 1, 1, 1, 1])
        self.clicked.insert(0, [1, 1, 1, 1, 1, 1, 1, 1, 1])
        for i in range(len(self.clicked)):
            self.clicked[i].insert(0, 1)
            self.clicked[i].append(1)

        i = 0
        while i != 10:
            randx = random.randint(0, 8)
            randy = random.randint(0, 8)
            if (self.mines[randx][randy] == 0) and ((randx != x) or (randy != y)):
                self.mines[randx][randy] = 9
                i += 1

        game_list[1:10, 1:10] = self.mines

        for i in range(1, 10):
            for j in range(1, 10):
                if game_list[i][j] != 9:
                    self.mines[i-1][j-1] = (game_list[i-1][j-1]+game_list[i-1][j]+game_list[i-1][j+1]+game_list[i][j-1]\
                    +game_list[i][j+1]+game_list[i+1][j-1]+game_list[i+1][j]+game_list[i+1][j+1]) // 9

    def draw_new_game(self):
        for i in range(9):
            for j in range(9):
                draw_square(i, j, self.display)

    def set_flag(self, x, y):
        (row, col) = xy2rowcol(x, y)
        if self.flags[row][col] == 1:
            self.flags[row][col] = 0
        else:
            self.flags[row][col] = 1

    def draw_flags(self):
        for i in range(9):
            for j in range(9):
                if self.flags[i][j] == 1:
                    draw_flag(self.display, i, j)

    def draw_squares(self, lost):
        for i in range(9):
            for j in range(9):
                if self.clicked[i+1][j+1] == 0 and (not lost or self.mines[i][j] != 9):
                    draw_square(i, j, self.display)
                elif lost:
                    if self.mines[i][j] == 9:
                        draw_mine(self.display, i, j)

    def draw_numbers(self):
        for i in range(9):
            for j in range(9):
                if (self.mines[i][j] != 0) and (self.mines[i][j] != 9):
                    number2screen(self.mines[i][j], self.display, i, j)

    def click_square(self, row, col):
        if self.clicked[row+1][col+1] == 1:
            return False
        elif self.mines[row][col] == 9:
            self.clicked[row + 1][col + 1] = 1
            return True
        elif self.mines[row][col] == 0:
            self.clicked[row+1][col+1] = 1
            for i in range(3):
                self.click_square(row+1-i, col)
                self.click_square(row+1-i, col+1)
                self.click_square(row+1-i, col-1)
            return False
        elif self.mines[row][col] != 9 and self.mines[row][col] != 0:
            self.clicked[row+1][col+1] = 1
            return False
        print(self.clicked)

