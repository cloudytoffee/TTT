# pylint: disable=C,wildcard-import

import pygame

import pygame_menu as pm
from include import const





class Main_Menu:

    def __init__(self,parent):
        self.menu_object = pm.Menu("Main Menu",
                                    const.constants["Menu"]["size"],
                                    const.constants["Menu"]["size"],
                                    theme= pm.themes.THEME_SOLARIZED,
                                    mouse_motion_selection=True)
        self.about = pm.Menu("About",const.constants["Menu"]["size"],
                                    const.constants["Menu"]["size"],
                                    theme= pm.themes.THEME_DEFAULT,
                                    mouse_motion_selection=True)
        self.about.add.button('Return to menu', pm.events.BACK)
        self.menu_object.add.selector('',[("X",True),("O",False)],
                                onchange=self.set_letter)
        self.menu_object.add.selector('',[("Beginner",0),("Easy",1),
                                ("Hard",2),("Impossible",3)],
                                onchange=self.set_difficulty)
        self.menu_object.add.button("Play",lambda: self.restart_game(parent))
        self.menu_object.add.button("About",self.about)
        self.menu_object.add.button("Quit",pm.events.EXIT)
        self.menu_object.mainloop(parent.surface)
    def set_letter(self,value, letter):
        pass
    def set_difficulty(self,value,difficulty):
        pass
    def restart_game(self, parent):
        self.menu_object.disable()
        self.menu_object.full_reset()
        parent.run()

