import pygame
<<<<<<< HEAD
import sys
=======
import sys, time
import pygame_menu as pm
>>>>>>> origin/main

from const import *
from game import Game
from square import Square
from move import Move
from ai import AI

<<<<<<< HEAD
=======
THEME_GREEN = (119, 154, 88)
THEME_WHITE = (255, 255, 255)
>>>>>>> origin/main

class Main:
    """The main class in which game work."""

    def __init__(self):
        pygame.init()
        # Set up the drawing window
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(caption)
        self.game = Game()
<<<<<<< HEAD
        self.ai = AI()
=======

        self.play_with_ai = True
        self.ai = AI()
        self.menu = None
        self.game_over_bool = False
        self.winner = None
        
    def create_menu(self):
        self.menu = pm.Menu(title="Chess Game",
                            width=WIDTH,
                            height=HEIGHT,
                            theme=pm.themes.THEME_GREEN)
        
        self.menu.add.button('Play', self.start_game)
        self.menu.add.button('Quit', self.quit_game)
        self.menu.add.selector('Theme:       ', [('Default', 1), ('Brawn', 2), ('Grey', 3), ('Blue', 4)], onchange=lambda value, _: self.game.change_theme(self.screen, value[1]))
        self.menu.add.selector('Player 2:       ', [('Bot', 1), ('2 Players', 2)], onchange=lambda value, setting: self.play_choice())
        
    def start_game(self):
        self.menu.disable()
        self.mainloop()

    def quit_game(self):
        pygame.quit()
        sys.exit()

    def game_over(self, winner):
        FONT_GAMEOVER = pygame.font.SysFont('Comic Sans', 120)
        FONT = pygame.font.SysFont('Arial', 60)
        FONT_BUTTON = pygame.font.SysFont('Arial', 30)
        # light shade of the button 
        color_light = (170,170,170) 
          
        # dark shade of the button 
        color_dark = (100,100,100) 
        #Text to render
        game_over_text = FONT_GAMEOVER.render("GAME OVER", True, pm.themes.THEME_GREEN.widget_font_color)
        score_text = FONT.render(f"Winner {winner}", True, pm.themes.THEME_GREEN.widget_font_color)
        button_menu = FONT_BUTTON.render("Start new game", True, pm.themes.THEME_GREEN.widget_font_color)
        button_quit = FONT_BUTTON.render("Quit", True, pm.themes.THEME_GREEN.widget_font_color)
        mouse = pygame.mouse.get_pos() 
        
        for ev in pygame.event.get(): 
          
            if ev.type == pygame.QUIT: 
                pygame.quit()
                sys.exit()
                  
            #checks if a mouse is clicked 
            if ev.type == pygame.MOUSEBUTTONDOWN: 
                  
                #if the mouse is clicked on the 
                # button the game is terminated 
                if WIDTH/2 <= mouse[0] <= WIDTH/2 + 50 + 280 and HEIGHT/2 <= mouse[1] <= HEIGHT/2 + 200 + 80:  
                    pygame.quit()
                    sys.exit()
                elif WIDTH/2 - 300 <= mouse[0] <= WIDTH/2 - 300 + 280 and HEIGHT/2 <= mouse[1] <= HEIGHT/2 + 200 + 80:
                    self.game_over_bool = False
                    self.game.reset()
                    game = self.game
                    board = self.game.board
                    dragger = self.game.dragger
        # fills the screen with a color 
        self.screen.fill(pm.themes.THEME_GREEN.background_color)

        # if mouse is hovered on a button it 
        # changes to lighter shade  
        if WIDTH/2 + 50 <= mouse[0] <= WIDTH/2 + 50 + 280 and HEIGHT/2 <= mouse[1] <= HEIGHT/2 + 200 + 80: 
            pygame.draw.rect(self.screen,color_light,[WIDTH/2+50,HEIGHT/2+200,280,80])
            pygame.draw.rect(self.screen,color_dark,[WIDTH/2-300,HEIGHT/2+200,280,80])
            self.screen.blit(button_menu, (WIDTH/2-260,HEIGHT/2+220))
            self.screen.blit(button_quit, (WIDTH/2+160,HEIGHT/2+220))
        elif WIDTH/2 - 300 <= mouse[0] <= WIDTH/2 - 300 + 280 and HEIGHT/2 <= mouse[1] <= HEIGHT/2 + 200 + 80: 
            pygame.draw.rect(self.screen,color_light,[WIDTH/2-300,HEIGHT/2+200,280,80])
            pygame.draw.rect(self.screen,color_dark,[WIDTH/2+50,HEIGHT/2+200,280,80])
            self.screen.blit(button_menu, (WIDTH/2-260,HEIGHT/2+220))
            self.screen.blit(button_quit, (WIDTH/2+160,HEIGHT/2+220))
        else: 
            pygame.draw.rect(self.screen,color_dark,[WIDTH/2-300,HEIGHT/2+200,280,80])
            pygame.draw.rect(self.screen,color_dark,[WIDTH/2+50,HEIGHT/2+200,280,80])
            self.screen.blit(button_menu, (WIDTH/2-260,HEIGHT/2+220))
            self.screen.blit(button_quit, (WIDTH/2+160,HEIGHT/2+220))
          
        # superimposing the text onto our button
        self.screen.blit(game_over_text, (WIDTH/2 - (game_over_text.get_width()/2), HEIGHT/2 - game_over_text.get_height()/2-200))
        self.screen.blit(score_text, (WIDTH/2 - (score_text.get_width()/2), (HEIGHT/2 + score_text.get_height() * 1.5 - 200)))
#         self.screen.blit(text , (WIDTH/2+50,HEIGHT/2))
        pygame.display.update()

    def play_choice(self):
        self.play_with_ai = not self.play_with_ai
>>>>>>> origin/main

    def mainloop(self):
        
        screen = self.screen
        game = self.game
        board = self.game.board
        dragger = self.game.dragger
        
        # Run until the user asks ti quit
        running = True
        while running:
            game.show_bg(screen)
            game.show_last_move(screen)
            game.show_moves(screen)
            game.show_pieces(screen)
            game.show_hover(screen)
            if dragger.dragging:
                dragger.update_blit(screen)
<<<<<<< HEAD
            if game.next_player == "black":
                piece = board.squares[self.ai.get_best_move(game.next_player, board)[0]][self.ai.get_best_move(game.next_player, board)[1]].piece
                initial = Square(self.ai.get_best_move(game.next_player, board)[0], self.ai.get_best_move(game.next_player, board)[1])
                final = Square(self.ai.get_best_move(game.next_player, board)[2], self.ai.get_best_move(game.next_player, board)[3])
                move = Move(initial, final)
                print(move)
                board.move(piece, move)
                board.set_true_en_passant(piece)
                # show methods
                game.show_bg(screen)
                game.show_last_move(screen)
                game.show_pieces(screen)
                # next turn
                game.next_turn()
=======
            
            if self.game_over_bool:
                self.game_over("WHITE")
            
            if self.play_with_ai:
                if game.next_player == "black":
                    bot_move = self.ai.get_best_move(game.next_player, board)
                    if bot_move is not None:
                        piece = bot_move[1]
                        move = bot_move[0]
                        board.move(piece, move)
                        board.set_true_en_passant(piece)
                        # show methods
                        game.show_bg(screen)
                        game.show_last_move(screen)
                        game.show_pieces(screen)
                        # next turn
                        game.next_turn()
                    else:
                        self.game_over_bool = True
>>>>>>> origin/main
            # Did the user click the window close button?
            for event in pygame.event.get():

                # click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    dragger.update_mouse(event.pos)

                    clicked_row = dragger.mouseY // SQSIZE
                    clicked_col = dragger.mouseX // SQSIZE

                    # if clicked square has a piece ?
                    if board.squares[clicked_row][clicked_col].has_piece():
                        piece = board.squares[clicked_row][clicked_col].piece
                        # valid piece (color) ?
                        if piece.color == game.next_player:
                            board.calc_moves(piece, clicked_row, clicked_col, bool=True)
                            dragger.save_initial(event.pos)
                            dragger.drag_piece(piece)
                            if len(piece.moves) == 0:
#                                 print(self.game_over_bool)
                                if piece.color == "black":
                                    self.winner = "white"
                                else:
                                    self.winner = "black"
                                self.game_over_bool = True
                                dragger.undrag_piece()
                            # show methods 
                            game.show_bg(screen)
                            game.show_last_move(screen)
                            game.show_moves(screen)
                            game.show_pieces(screen)
                
                # mouse motion
                elif event.type == pygame.MOUSEMOTION:
                    motion_row = event.pos[1] // SQSIZE
                    motion_col = event.pos[0] // SQSIZE

                    game.set_hover(motion_row, motion_col)

                    if dragger.dragging:
                        dragger.update_mouse(event.pos)
                        # show methods
                        game.show_bg(screen)
                        game.show_last_move(screen)
                        game.show_moves(screen)
                        game.show_pieces(screen)
                        game.show_hover(screen)
                        dragger.update_blit(screen)
                
                # click release
                elif event.type == pygame.MOUSEBUTTONUP:
                    
                    if dragger.dragging:
                        dragger.update_mouse(event.pos)

                        released_row = dragger.mouseY // SQSIZE
                        released_col = dragger.mouseX // SQSIZE

                        # create possible move
                        initial = Square(dragger.initial_row, dragger.initial_col)
                        final = Square(released_row, released_col)
                        move = Move(initial, final)
                        print(move)

                        # valid move ?
                        if board.valid_move(dragger.piece, move):
                            # normal capture
                            captured = board.squares[released_row][released_col].has_piece()
                            board.move(dragger.piece, move)

                            board.set_true_en_passant(dragger.piece)                            

                            # sounds
                            game.play_sound(captured)
                            # show methods
                            game.show_bg(screen)
                            game.show_last_move(screen)
                            game.show_pieces(screen)
                            # next turn
                            game.next_turn()
                    dragger.undrag_piece()
                
                # key press
                elif event.type == pygame.KEYDOWN:
                    
                    # changing themes
                    if event.key == pygame.K_RETURN:
                        game.change_theme(self.screen, 1)

                     # changing themes
                    if event.key == pygame.K_r:
                        game.reset()
                        game = self.game
                        board = self.game.board
                        dragger = self.game.dragger

                # quit application
                elif event.type == pygame.QUIT:
                    self.quit_game()
            
            pygame.display.update()


main = Main()
main.mainloop()