<<<<<<< HEAD
from sklearn.tree import DecisionTreeClassifier
from const import *
import sys
from square import Square
from move import Move

class AI:
    def __init__(self, depth=2):
        self.depth = depth
        self.piece = None

    # Define function to get all possible moves for a player
    def get_all_moves(self, player, board):
        moves = []
        for row in range(ROWS):
            for col in range(COLS):
#                 if board[row][col].isupper() == player:
                    for i in range(-2, 3):
                        for j in range(-2, 3):
                            if (i, j) != (0, 0) and row + i >= 0 and row + i < ROWS and col + j >= 0 and col + j < COLS:
#                                 piece = board.squares[row][col].piece
#                                 initial = square(row, col)
#                                 final = square(row + i, col + j)
#                                 move = Move(initial, final)
#                                 if board.valid_move(piece, move):
                                    moves.append((row, col, row + i, col + j))
        return moves

    # Define function to get best move for AI opponent using decision tree model
    def get_best_move(self, player, board):
        X = []
        y = []
        for move in self.get_all_moves(player, board):
#             X.append([board[move[0]][move[1]], move[1], move[0], move[3], move[2]])
#             board_copy = [row[:] for row in board]
#             row = move[0]
#             col = move[1]
#             piece = board.squares[row][col].piece
#             print(piece)
#             initial = Square(row, col)
#             final = Square(move[2], move[3])
#             move = Move(initial, final)
#             board.move(piece, move)
#             score = evaluate_board()
#             board = [row[:] for row in board_copy]
#             y.append(score)
#         clf = DecisionTreeClassifier()
#         clf.fit(X, y)
#         move = clf.predict([[player, 0, 0, 0, 0]])[0]
            return [move[0], move[1], move[2], move[3]]
=======
from const import *
import sys
from game import Game
from move import Move
from square import Square
import numpy as np
from random import randint


class AI:
    def __init__(self, depth=0):
        self.depth = depth
        self.piece = None
        self.game = Game()
        self.made_steps = []

    # Define function to get all possible moves for a player
    def get_all_moves(self, player, board):
        c_moves = []
        moves = []
        for row in range(ROWS):
            for col in range(COLS):
                if board.squares[row][col].has_piece():
                    piece = board.squares[row][col].piece
                    if piece.color == "black":
                        if board.squares[row][col].has_enemy_piece("black"):
                            c_moves.append((row, col))
                        else:
                            moves.append((row, col))
        return [moves, c_moves]
        

    # Define function to get best move for AI opponent using decision tree model
    def get_best_move(self, player, board):
        king_alive = False
        cryt_moves = []
        moves = []
        if len(self.get_all_moves(player, board)[1]) == 0:
            for move in self.get_all_moves(player, board)[0]:
                piece = board.squares[move[0]][move[1]].piece
                if piece.name == "king":
                    king_alive = True
                board.calc_moves(piece, move[0], move[1])
                for new_move in piece.moves:
                    move = new_move
                    if board.valid_move(piece, move):
                        if not board.in_check(piece, move):
                            if board.squares[new_move.final.row][new_move.final.col].has_enemy_piece("black"):
                                if piece.name == "pawn":
                                    if move.initial.col != move.final.col:
                                        cryt_moves.append([move, piece])
                                else:
                                    cryt_moves.append([move, piece])
                            else:
                                if board.squares[new_move.final.row][new_move.final.col].isempty_or_enemy("black"):
                                    moves.append([move, piece])
        if king_alive:
            if len(cryt_moves) > 0:
                return cryt_moves[0]
            else:
                if len(moves) > 0:
                    valik = randint(0, len(moves)-1)
                    return moves[valik]
        else:
            return None

>>>>>>> origin/main
