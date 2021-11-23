# TIC TAC TOE by (legal name Ahil, preffered name Bea), 2021
import random
import pygame
import pygame_menu as pm
import time
from include import const, functions


# main class of board, handles most of the logic and GUI
class Board:

# initialise the class with the correct menus and other variables
    def __init__(self):
        pygame.init()  # init pygame
        self.clock = pygame.time.Clock()  # make a pygame clock var
        self.surface = pygame.display.set_mode(
            (const.constants["Game"]["width"],
             const.constants["Game"]["height"]))
        self.running = True
        self.winner = None
        self.message = ''
        self.letter = True
        self.current_letter = True
        self.board = [None]*9
        # main instance of the pygame meny module for the main menu
        self.menu_object = pm.Menu("Main Menu",
                                   const.constants["Menu"]["size"],
                                   const.constants["Menu"]["size"],
                                   theme=pm.themes.THEME_SOLARIZED,
                                   mouse_motion_selection=True)
        # create an instance of the pygame menu for the about page
        self.about = pm.Menu("About", const.constants["Menu"]["size"],
                             const.constants["Menu"]["size"],
                             theme=pm.themes.THEME_DEFAULT,
                             mouse_motion_selection=True)
        # create an instance of the pygame menu for the play again scene
        self.again = pm.Menu("Game over", const.constants["Game"]["size"],
                             const.constants["Game"]["height"],
                             theme=pm.themes.THEME_DARK,
                             mouse_motion_selection=True)
        self.again.add.button('Return to menu', self.restart)
        for a in const.ABOUT:
            self.about.add.label(a, margin=(0, 0), font_size=20)
        self.about.add.button('Return to menu', pm.events.BACK)
        self.about.add.vertical_margin(30)
        # add buttons to the main menu
        self.menu_object.add.button("Play", self.main_game_loop)
        self.menu_object.add.button("About", self.about)
        self.menu_object.add.button("Quit", pm.events.EXIT)

    def main_background(self) -> None:  # create main background callable
        self.surface.fill((255, 255, 255))

    def restart(self) -> None:  # fully reset the instance
        self.__init__()
        self.run()

    def draw_cross(self) -> None:  # draw the '#' shape for the board
        self.surface.fill((255, 255, 255))  # fill the screen with white
        pygame.draw.line(self.surface, (0, 0, 0),
                         ((const.constants["Game"]["size"]) / 3, 0),
                         ((const.constants["Game"]["size"]) / 3,
                         (const.constants["Game"]["size"])), 7)
        pygame.draw.line(self.surface, (0, 0, 0),
                         ((const.constants["Game"]["size"]) / 3 * 2, 0),
                         ((const.constants["Game"]["size"]) / 3 * 2,
                         (const.constants["Game"]["size"])), 7)
        pygame.draw.line(self.surface, (0, 0, 0),
                         (0, (const.constants["Game"]["size"]) / 3),
                         ((const.constants["Game"]["size"]),
                         (const.constants["Game"]["size"]) / 3), 7)
        pygame.draw.line(self.surface, (0, 0, 0),
                         (0, (const.constants["Game"]["size"]) / 3 * 2),
                         ((const.constants["Game"]["size"]),
                         (const.constants["Game"]["size"]) / 3 * 2), 7)

# check where the click was, and assign which box it was clicked in 
    def checkClick(self) -> None:
        x, y = pygame.mouse.get_pos()

        # assign rows and coloumns of the click 
        if (x < const.constants["Game"]["width"] / 3):
            self.col = 0
        elif (x < (const.constants["Game"]["width"] / 3 * 2)):
            self.col = 1
        elif (x < const.constants["Game"]["width"]):
            self.col = 2
        else:
            self.col = None
        if (y < const.constants["Game"]["height"] / 3):
            self.row = 0
        elif (y < (const.constants["Game"]["height"] / 3 * 2)):
            self.row = 1
        elif (y < const.constants["Game"]["height"]):
            self.row = 2
        else:
            self.row = None

        # assign the position from coloumns and rows
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
        # blit the current letter in the correct place
        if self.current_letter:
            if self.board[self.pos] is None:
                self.drawLetter(self.row, self.col, self.current_letter)
                self.board[self.pos] = False
                self.current_letter = not self.current_letter
                self.blitMessage(self.current_letter)
        else:
            if self.board[self.pos] is None:
                self.drawLetter(self.row, self.col, self.current_letter)
                self.board[self.pos] = True
                self.current_letter = not self.current_letter
                self.blitMessage(self.current_letter)
        print(self.board)

# Draw the letter chosen on the screen in the correct place
    def drawLetter(self, row, col, letter) -> None:
        if row == 0:
            posx = 30
        if row == 1:
            posx = const.constants["Game"]["width"] / 3 + 30
        if row == 2:
            posx = const.constants["Game"]["width"] / 3 * 2 + 30
        if col == 0:
            posy = 30
        if col == 1:
            posy = const.constants["Game"]["height"] / 3 + 30
        if col == 2:
            posy = const.constants["Game"]["height"] / 3 * 2 + 30
        if letter:
            self.surface.blit(const.o_letter, (posy, posx))
        else:
            self.surface.blit(const.x_letter, (posy, posx))
        pygame.display.update()

# check to see if anyone has won the game yet, or if it is a draw
    def checkWin(self, board) -> None:
        win_x = functions.isWinner(board, self.letter)
        if win_x:
            self.again.add.label("GAME OVER\n X WINS",
                                 align=pm.locals.ALIGN_CENTER, font_size=50)
            self.again.add.button("Quit", pm.events.EXIT)
            time.sleep(0.5)  # wait a bit to let people recognise
            self.again.mainloop(self.surface,
                                self.main_background, fps_limit=15)
        win_o = functions.isWinner(board, (not self.letter))
        if win_o:
            self.again.add.label("GAME OVER\n O WINS",
                                 align=pm.locals.ALIGN_CENTER, font_size=50)
            self.again.add.button("Quit", pm.events.EXIT)
            time.sleep(0.5)  # wait a bit to let people recognise
            self.again.mainloop(self.surface,
                                self.main_background, fps_limit=15)
        if functions.boardFull(board):
            self.again.add.label("GAME OVER\n TIE",
                                 align=pm.locals.ALIGN_CENTER, font_size=50)
            self.again.add.button("Quit", pm.events.EXIT)
            time.sleep(0.5)  # wait a bit to let people recognise
            self.again.mainloop(self.surface,
                                self.main_background, fps_limit=15)
        else:
            return

# this prints the current letter to play
    def blitMessage(self, letter) -> None:
        if letter:
            self.message = "O's Turn!"
        else:
            self.message = "X's Turn!"
        self.font = pygame.font.Font(None, 26)
        self.text = self.font.render(self.message, 1, (255, 255, 255))
        self.surface.fill((0, 0, 0), (0, 900, 950, 50))  # make a black rect
        self.text_rect = self.text.get_rect(center=(const.constants["Game"]
                                            ["size"] / 2, 925))
        self.surface.blit(self.text, self.text_rect)  # draw the text
        pygame.display.update()  # update the display

# the main loop, which shows the menu screen
    def run(self) -> None:
        while self.running:
            self.clock.tick(15)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False  # quit if needed
            if self.menu_object.is_enabled():
                self.menu_object.mainloop(self.surface,  # enable the menu
                                          self.main_background, fps_limit=15)
            pygame.display.update()  # update the display
        pygame.quit()

# this is the main game loop, where the tic tac toe game window is shown
    def main_game_loop(self) -> None:
        self.board = [None]*9  # reset the board
        self.menu_object.disable()  # close the menu window
        self.draw_cross()  # draw the cross for the display
        self.blitMessage(self.current_letter)  # display the current player's time
        while True:
            self.clock.tick(15)
            pygame.display.update()
            events = pygame.event.get()
            for e in events:
                if e.type == pygame.QUIT:
                    exit()  
                elif e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        self.menu_object.enable()  # if the escape key is pressed, go to main menu
                        return
                elif e.type == pygame.MOUSEBUTTONDOWN:
                    self.checkClick()  # check where the click went
                    self.checkWin(self.board)  # check for winner
            if self.menu_object.is_enabled():
                self.menu_object.update(events)  # update the menu
