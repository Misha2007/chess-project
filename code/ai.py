from sklearn.tree import DecisionTreeClassifier
from const import *
import sys
from game import Game
from move import Move
from square import Square
import random

class AI:
    def __init__(self, depth=0):
        self.depth = depth
        self.piece = None
        self.game = Game()
        self.made_steps = []

    # Define function to get all possible moves for a player
    def get_all_moves(self, player, board):
        moves = []
        for row in range(ROWS):
            for col in range(COLS):
                moves.append((row, col))
        return moves

#     def get_moves_by_piece(self, player, board):
#         x = []
# #         if piece is not None:
# #         print(self.get_all_moves(player, board))
#         for step in self.get_all_moves(player, board):
# #         while is_true:
# #             x_step = random.randint(0, 7)
# #             y_step = random.randint(0, 7)
# #             self.get_all_moves(self, player, board)
# #             step = [x_step, y_step]
#             piece = board.squares[step[0]][step[1]].piece
#             if piece is not None and piece.color == player:
#                 board.calc_moves(piece, step[0], step[1], bool=True)
# #                 return piece.moves
#                 for piece_move in self.get_moves_by_piece(player, board):
# #                         move = Move(piece_move.initial, piece_move.final)
#                         if board.valid_move(piece, piece_move) and [piece_move.initial, piece_move.final, piece] not in self.made_steps:
#                             print(piece.moves)
# #                             list_steps = [piece, move]
#                             x.append([piece_move.initial, piece_move.final, piece])
# #                                 is_true = True
# #             else:
# #                 print("sd")
#         if len(x) > 0:
#             return x
                            
        

    # Define function to get best move for AI opponent using decision tree model
    def get_best_move(self, player, board):
        x = []
        board = self.game.board
        for step in self.get_all_moves(player, board):
#         while is_true:
#             x_step = random.randint(0, 7)
#             y_step = random.randint(0, 7)
#             self.get_all_moves(self, player, board)
#             step = [x_step, y_step]
            piece = board.squares[step[0]][step[1]].piece
            if piece is not None and piece.color == player:
                board.calc_moves(piece, step[0], step[1], bool=True)
                for piece_move in piece.moves:
# #                         move = Move(piece_move.initial, piece_move.final)
                        if board.valid_move(piece, piece_move) and [piece_move.initial, piece_move.final, piece] not in self.made_steps:
# #                             print(board.squares[piece_move.final.row][piece_move.final.col].has_piece(piece.color))
                            if board.squares[piece_move.final.row][piece_move.final.col].has_enemy_piece(piece.color):
#                             list_steps = [piece, move]
                                x.append([piece_move.initial, piece_move.final, piece])
                                is_true = True
                                break
                            else:
                                x.append([piece_move.initial, piece_move.final, piece])
                        else:
                            piece = board.squares[step[0]][step[1]].piece
        if len(x) > 0:
            self.made_steps.append(x[-1])
            print(self.made_steps[-1])
            is_true = True
            return self.made_steps[-1]
#             if len(self.made_steps) > 0:
#                 is_true = True
#                 x = []
#                 return self.made_steps[-1]
#         print(x)
#                 self.made_steps.pop(-1)
#                 if len(self.made_steps) > 1:
#                     del self.made_steps[-1]
#             self.made_steps.append(x[-1])
#                 print(self.made_steps[-1])
#             is_true = True
#                 x = []
#         return self.get_moves_by_piece(player, board)
#                 self.made_steps.append(x[-1])


