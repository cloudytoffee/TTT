import pygame
import pygame_menu as pm
from include import const,menu


class Board:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.surface = pygame.display.set_mode(
            (const.constants["Game"]["size"],
            const.constants["Game"]["size"]))
        self.running = True
        self.gaming = True
        
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
        self.about.add.vertical_margin(30)
        self.menu_object.add.selector('',[("X",True),("O",False)],
                                onchange=self.set_letter)
        self.menu_object.add.selector('',[("Beginner",0),("Easy",1),
                                ("Hard",2),("Impossible",3)],
                                onchange=self.set_difficulty)
        self.menu_object.add.button("Play",self.main_game_loop)
        self.menu_object.add.button("About",self.about)
        self.menu_object.add.button("Quit",pm.events.EXIT)
        
        
        
    def main_background(self) -> None:
        """
        Function used by menus, draw on background while menu is active.
        :return: None
        """
        self.surface.fill((128, 0, 128))


    def set_letter(self,value, letter):
        pass
    def set_difficulty(self,value,difficulty):
        pass    
    def run(self):
        while self.running:
            self.clock.tick(60)
            self.main_background()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            if self.menu_object.is_enabled():
                self.menu_object.mainloop(self.surface,self.main_background,fps_limit=60)
            pygame.display.flip()
        pygame.quit()
        
    def main_game_loop(self):
        frame=0
        print("gaming")
        self.menu_object.disable()
        self.menu_object.full_reset()
        while self.gaming:
            self.clock.tick(60)
            frame += 1
            events = pygame.event.get()
            for e in events:
                if e.type == pygame.QUIT:
                    exit()
                elif e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        self.menu_object.enable()
                        return
            if self.menu_object.is_enabled():
                self.menu_object.update(events)
            self.surface.fill((0,0,0))
            if frame ==100:
                break