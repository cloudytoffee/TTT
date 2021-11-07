#pylint: disable=C,unspecified-encoding
import json
import os
import pygame as pg
with open(r'source\include\constants.json','r') as c:
    constants = json.load(c)

x_letter = pg.image.load(os.path.join("source","include","data","x_letter.gif"))
o_letter = pg.image.load(os.path.join("source","include","data","o_letter.gif"))