import random 
import pygame
import pygame_menu as pm
import time
from include import const, functions


class Board:

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.surface = pygame.display.set_mode(
            (const.constants["Game"]["width"],
            const.constants["Game"]["height"]))
        self.running = True
        self.winner = None
        self.message = ''
        self.letter = True
        self.current_letter = True
        self.board = [None]*9
        print(self.board)
        self.menu_object = pm.Menu("Main Menu",
                                    const.constants["Menu"]["size"],
                                    const.constants["Menu"]["size"],
                                    theme= pm.themes.THEME_SOLARIZED,
                                    mouse_motion_selection=True)

        self.about = pm.Menu("About",const.constants["Menu"]["size"],
                                    const.constants["Menu"]["size"],
                                    theme= pm.themes.THEME_DEFAULT,
                                    mouse_motion_selection=True)
        self.again = pm.Menu("Game over",const.constants["Game"]["size"],
                                    const.constants["Game"]["height"],
                                    theme= pm.themes.THEME_DARK,
                                    mouse_motion_selection=True )
        self.again.add.button('Return to menu', self.restart)
        for a in const.ABOUT:
            self.about.add.label(a,margin=(0,0),font_size=20)
        self.about.add.button('Return to menu', pm.events.BACK)
        self.about.add.vertical_margin(30)
        self.menu_object.add.button("Play",self.main_game_loop)
        self.menu_object.add.button("About",self.about)
        self.menu_object.add.button("Quit",pm.events.EXIT)

    def main_background(self) -> None:
        self.surface.fill((255,255,255))

    def restart(self):
        self.__init__()
        self.run()

    def draw_cross(self) ->  None: 
        self.surface.fill((255,255,255))
        pygame.draw.line(self.surface, (0,0,0),
                        ((const.constants["Game"]["size"]) / 3, 0),
                        ((const.constants["Game"]["size"])/ 3,
                        (const.constants["Game"]["size"])), 7)
        pygame.draw.line(self.surface, (0,0,0),
                        ((const.constants["Game"]["size"]) / 3 * 2, 0),
                        ((const.constants["Game"]["size"])/ 3 * 2, 
                        (const.constants["Game"]["size"])), 7)
        pygame.draw.line(self.surface, (0,0,0),
                        (0, (const.constants["Game"]["size"]) / 3),
                        ((const.constants["Game"]["size"]),
                        (const.constants["Game"]["size"]) / 3), 7)
        pygame.draw.line(self.surface, (0,0,0),
                        (0, (const.constants["Game"]["size"]) / 3 * 2),
                        ((const.constants["Game"]["size"]),
                        (const.constants["Game"]["size"]) / 3 * 2), 7)
        

    def checkClick(self):
        x,y = pygame.mouse.get_pos()
        if (x<const.constants["Game"]["width"] / 3):
            self.col = 0
        elif (x<(const.constants["Game"]["width"] /3 *2)):
            self.col = 1
        elif (x< const.constants["Game"]["width"] ):
            self.col = 2
        else:
            self.col = None
        if (y<const.constants["Game"]["height"] / 3):
            self.row = 0
        elif (y<(const.constants["Game"]["height"] /3 *2)):
            self.row = 1
        elif (y< const.constants["Game"]["height"] ):
            self.row = 2
        else:
            self.row = None

        if self.row == 0 and self.col == 0:
            self.pos = 0
        elif self.row == 0 and self.col == 1:
            self.pos = 1
        elif self.row == 0 and self.col == 2:
            self.pos = 2
        elif self.row == 1 and self.col == 0:
            self.pos = 3
        elif self.row == 1 and self.col == 1:
            self.pos = 4
        elif self.row == 1 and self.col == 2:
            self.pos = 5
        elif self.row == 2 and self.col == 0:
            self.pos = 6
        elif self.row == 2 and self.col == 1:
            self.pos = 7
        elif self.row == 2 and self.col == 2:
            self.pos = 8
        if self.current_letter:
            if self.board[self.pos] == None:
                self.drawLetter(self.row, self.col,self.current_letter)
                self.board[self.pos] = False
                self.current_letter = not self.current_letter
                self.blitMessage(self.current_letter)
        else:
            if self.board[self.pos] == None:
                self.drawLetter(self.row, self.col,self.current_letter)
                self.board[self.pos] = True
                self.current_letter = not self.current_letter
                self.blitMessage(self.current_letter)
        print(self.board)


    def drawLetter (self,row,col,letter):
        if row == 0:
            posx = 30
        if row == 1:
            posx = const.constants["Game"]["width"] / 3 + 30
        if row == 2:
            posx = const.constants["Game"]["width"]/ 3 * 2 + 30
        if col == 0:
            posy = 30
        if col == 1:
            posy = const.constants["Game"]["height"] / 3 + 30
        if col == 2:
            posy = const.constants["Game"]["height"] / 3 * 2 + 30
        if letter:
            self.surface.blit(const.o_letter,(posy,posx))
        else:
            self.surface.blit(const.x_letter,(posy,posx))
        pygame.display.update()

    def checkWin (self, board):
        win_x = functions.isWinner(board,self.letter)
        if win_x:
            self.again.add.label("GAME OVER\n X WINS",align=pm.locals.ALIGN_CENTER, font_size=50)
            self.again.add.button("Quit",pm.events.EXIT)
            time.sleep(0.5)
            self.again.mainloop(self.surface,self.main_background,fps_limit=15)
        win_o = functions.isWinner(board,(not self.letter))
        if win_o:
            self.again.add.label("GAME OVER\n O WINS",align=pm.locals.ALIGN_CENTER, font_size=50)
            self.again.add.button("Quit",pm.events.EXIT)
            time.sleep(0.5)
            self.again.mainloop(self.surface,self.main_background,fps_limit=15)
        if functions.boardFull(board):
            self.again.add.label("GAME OVER\n TIE",align=pm.locals.ALIGN_CENTER, font_size=50)
            self.again.add.button("Quit",pm.events.EXIT)
            time.sleep(0.5)
            self.again.mainloop(self.surface,self.main_background,fps_limit=15)
        else:
            return

    def blitMessage (self,letter):
        if letter:
            self.message = "O's Turn!"
        else:
            self.message = "X's Turn!"
        self.font = pygame.font.Font(None, 26)
        self.text = self.font.render(self.message,1,(255,255,255))
        self.surface.fill((0,0,0),(0,900,950,50))
        self.text_rect = self.text.get_rect(center =(const.constants["Game"]["size"]/2, 925))
        self.surface.blit(self.text,self.text_rect)
        pygame.display.update()

    def run(self):
        while self.running:
            self.clock.tick(15)
            self.draw_cross()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            if self.menu_object.is_enabled():
                self.menu_object.mainloop(self.surface,self.main_background,fps_limit=15)
            pygame.display.update()
        pygame.quit()

    def main_game_loop(self):
        self.menu_object.disable()
        self.draw_cross()
        self.blitMessage(self.current_letter)
        while True:
            self.clock.tick(15)
            pygame.display.update()
            events = pygame.event.get()
            for e in events:
                if e.type == pygame.QUIT:
                    exit()
                elif e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        self.menu_object.enable()
                        return
                elif e.type == pygame.MOUSEBUTTONDOWN:
                    self.checkClick()
                    self.checkWin(self.board)
            if self.menu_object.is_enabled():
                self.menu_object.update(events)