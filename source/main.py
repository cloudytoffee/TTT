# pylint: disable=C,unspecified-encoding

import sys
import menu

# C= False

# pygame.init()
# window = pygame.display.set_mode((constants["Main"]["size"],constants["Main"]["size"]))
# pygame.display.set_caption("Main Menu")

# def change_game(selected:Tuple, value:Any):
#     C = value
#     print(f" changed game to{(selected[0])}({value})")


# def start_game():
#     if C is True:
#         pygame.display.set_caption("2048")
#         pygame.display.set_mode((constants["_2048"]["size"],constants["_2048"]["size"]))
#     else:
#         pygame.display.set_caption("Tetris")
#         pygame.display.set_mode((constants["Tetris"]["height"],constants["Tetris"]["width"]))

# menu = pm.Menu("Menu",constants["Main"]["size"],constants["Main"]["size"],theme=pm.themes.THEME_SOLARIZED)
# menu.add.selector("Game:",[("2048",True),("Tetris",False)],onchange= change_game)
# menu.add.button('Play',start_game)
# menu.add.button('Quit', pm.events.EXIT)

# menu.mainloop(window)

if __name__ == "__main__":
    menu.App().run()
sys.exit()
