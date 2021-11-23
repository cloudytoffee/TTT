#pylint: disable=C,unspecified-encoding
import json
import os
import pygame as pg
with open(r'source/include/options.json','r') as c:
    constants = json.load(c)

x_letter = pg.image.load(os.path.join("source","include","data","x_letter.gif"))
o_letter = pg.image.load(os.path.join("source","include","data","o_letter.gif"))

ABOUT = [f'This is a simple GUI based two player TIC TAC TOE game',
        f'The menus are made using the pygame-menu module,',
        f'And the game is made using some simple logic',
        f'This was originally meant to have computer controlled moves',
        f'with varying difficulty levels,',f'but my procrastination and work ethic',
        f'along with a large amount of stress from lockdown and exams',
        f'made for a very mediocre result',
        f'Anyway, just click on the squares',f'like you would usually play TicTacToe',
        f'If you get three of your letters in a row, you would win the game!',
        f'O starts',f'Have fun playing.']