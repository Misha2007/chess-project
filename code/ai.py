from sklearn.tree import DecisionTreeClassifier
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
#                                             print([row, col])
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
#                 print(piece)
                for new_move in piece.moves:
                    move = new_move
                    if board.valid_move(piece, move):
                        if board.squares[new_move.final.row][new_move.final.col].has_enemy_piece("black"):
                            if piece.name == "pawn":
                                if move.initial.col != move.final.col:
                                    cryt_moves.append([move, piece])
                            else:
                                cryt_moves.append([move, piece])
                        else:
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

