import random 
import pygame
import pygame_menu as pm
import time
from include import const,functions


class Board:

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.surface = pygame.display.set_mode(
            (const.constants["Game"]["width"],
            const.constants["Game"]["height"]))
        self.turn_number = 0
        self.running = True
        self.gaming = True
        self.winner = None
        self.message = ''
        self.player_first = False
        self.letter = True
        self.difficulty = 0
        self.current_letter = functions.startingPlayer()
        if self.letter == self.current_letter:
            self.player_first = True

        self.board = [' ']*9
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
        self.again.add.button('Play again', self.restart)
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
        self.surface.fill((255,255,255))
    def restart(self):
        self.__init__()
        self.run()
    def set_letter(self,value, letter):
        self.letter = letter
        # print(self.letter)
        pass

    def set_difficulty(self,value,difficulty):
        self.difficulty = difficulty
        # print(self.difficulty)
        pass

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
        

    def checkClick(self,computer,move):
        if computer:
            if self.letter:
                self.board[move] = True
            else:
                self.board[move] = False
            return
        x,y = pygame.mouse.get_pos()
        if (x<const.constants["Game"]["width"] / 3):
            self.col = 0
            # print('c0')
        elif (x<(const.constants["Game"]["width"] /3 *2)):
            self.col = 1
            # print('c1')
        elif (x< const.constants["Game"]["width"] ):
            self.col = 2
            # print('c2')
        else:
            self.col = None
        if (y<const.constants["Game"]["height"] / 3):
            self.row = 0
            # print('r0')
        elif (y<(const.constants["Game"]["height"] /3 *2)):
            self.row = 1
            # print('r1')
        elif (y< const.constants["Game"]["height"] ):
            self.row = 2
            # print('r2')
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
            if self.board[self.pos] == " ":
                self.drawLetter(self.row, self.col,self.current_letter,False,None)
                self.board[self.pos] = True
                self.current_letter = not self.current_letter
        else:
            if self.board[self.pos] == " ":
                self.drawLetter(self.row, self.col,self.current_letter,False,None)
                self.board[self.pos] = False
                self.current_letter = not self.current_letter
        print(self.board)


    def drawLetter (self,row,col,letter,computer,move):
        if computer:
            if move == 0:
                posx, posy = 30, 30
            if move == 1:
                posx, posy = const.constants["Game"]["width"] / 3 + 30, 30
            if move == 2:
                posx, posy = const.constants["Game"]["width"]/ 3 * 2 + 30, 30
            if move == 3:
                posx, posy = 30, const.constants["Game"]["height"] / 3 + 30
            if move == 4:
                posx, posy = const.constants["Game"]["width"] / 3 + 30, const.constants["Game"]["height"] / 3 + 30
            if move == 5:
                posx, posy = const.constants["Game"]["width"]/ 3 * 2 + 30, const.constants["Game"]["height"] / 3 + 30
            if move == 6:
                posx, posy = 30, const.constants["Game"]["height"] / 3 * 2 + 30
            if move == 7:
                posx, posy = const.constants["Game"]["width"] / 3 + 30, const.constants["Game"]["height"] / 3 * 2 + 30
            if move == 8:
                posx, posy = const.constants["Game"]["width"]/ 3 * 2 + 30, const.constants["Game"]["height"] / 3 * 2 + 30
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
        if computer:
            if letter:
                self.surface.blit(const.o_letter,(posy,posx))
            else:
                self.surface.blit(const.x_letter,(posy,posx))
        else:
            if letter:
                self.surface.blit(const.o_letter,(posy,posx))
            else:
                self.surface.blit(const.x_letter,(posy,posx))
        pygame.display.update()

    def checkWin (self, board):
        win_player = functions.isWinner(board,self.letter)
        if functions.boardFull(board):
            print('draw')
            self.again.add.label("GAME OVER\n TIE",align=pm.locals.ALIGN_CENTER, font_size=60)
            self.again.add.button("Quit",pm.events.EXIT)
            time.sleep(1)
            self.again.mainloop(self.surface,self.main_background,fps_limit=60)
        if win_player:
            print('player wins')
            self.again.add.label("GAME OVER\n PLAYER WINS",align=pm.locals.ALIGN_CENTER, font_size=60)
            self.again.add.button("Quit",pm.events.EXIT)
            time.sleep(1)
            self.again.mainloop(self.surface,self.main_background,fps_limit=60)
        win_comp = functions.isWinner(board,(not self.letter))
        if win_comp:
            print('comp wins')
            self.again.add.label("GAME OVER\n COMPUTER WINS",align=pm.locals.ALIGN_CENTER, font_size=60)
            self.again.add.button("Quit",pm.events.EXIT)
            time.sleep(1)
            self.again.mainloop(self.surface,self.main_background,fps_limit=60)
        else:
            return

    def run(self):
        while self.running:
            self.clock.tick(60)
            self.draw_cross()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            if self.menu_object.is_enabled():
                self.menu_object.mainloop(self.surface,self.main_background,fps_limit=60)
            pygame.display.update()
        pygame.quit()

    def main_game_loop(self):
        print("gaming")
        self.menu_object.disable()
        self.draw_cross()
        while self.gaming:
            self.clock.tick(60)
            pygame.display.update()
            events = pygame.event.get()
            if self.player_first:
                for e in events:
                    if e.type == pygame.QUIT:
                        exit()
                    elif e.type == pygame.KEYDOWN:
                        if e.key == pygame.K_ESCAPE:
                            self.menu_object.enable()
                            return
                    elif e.type == pygame.MOUSEBUTTONDOWN:
                        self.checkClick(False,None)
                        self.checkWin(self.board)
                        self.player_first = not self.player_first
                if self.menu_object.is_enabled():
                    self.menu_object.update(events)
                
            else:
                self.turn_number += 1
                for e in events:
                    if e.type == pygame.QUIT:
                        exit()
                    elif e.type == pygame.KEYDOWN:
                        if e.key == pygame.K_ESCAPE:
                            self.menu_object.enable()
                            return
                if self.menu_object.is_enabled():
                    self.menu_object.update(events)
                move = functions.getCompMove(self.board,(not self.letter),self.player_first,self.turn_number,self.difficulty)
                print(move)
                self.checkClick(True,move)
                self.drawLetter(None,None,self.letter,True,move)
                self.checkWin(self.board)
                self.player_first = not self.player_first