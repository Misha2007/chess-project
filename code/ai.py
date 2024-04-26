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
