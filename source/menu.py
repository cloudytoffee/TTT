# pylint: disable=C,wildcard-import
import pygame
import pygame_menu as pm
from include import const

class App:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode(
            (const.constants["Game"]["size"],
            const.constants["Game"]["size"]))
        self.menu = pm.Menu("Main Menu", const.constants["Menu"]["size"],
                                    const.constants["Menu"]["size"],
                                    theme= pm.themes.THEME_SOLARIZED)
        self.menu.add.selector('Player Letter:',[("X",True),("O",False)],
                                onchange=self.set_letter)
        self.menu.add.selector('Comp Difficulty :',
                                [("Beginner",1),("Easy",2),
                                ("Hard",3),("Impossible",4)],
                                onchange=self.set_difficulty)
        
        self.menu.add.button("Play",self.restart_game)
        self.menu.add.button("Quit",pm.events.EXIT)
        self.menu.mainloop(self.surface)
    def set_letter(self,value, letter):
        pass
    def set_difficulty(self,value,difficulty):
        pass
    def restart_game(self):
        pass