import numpy as np
from copy import deepcopy
from constants import DIMENSION, FREE, PLAYER_1, PLAYER_2
from helpers import my_pieces, adjacent_positions, max_aligned_pieces, adjacent_pieces, islands, is_valid_move, is_free, total_components, total_adjacents


class Game(object):

    def __init__(self):
        while True:  # Construct a non-winner board
            board = np.repeat(FREE, DIMENSION*DIMENSION)
            initial_positions = np.random.choice(25, 8, replace=False)
            board[initial_positions[0:4]] = PLAYER_1
            board[initial_positions[4:8]] = PLAYER_2
            board.resize([DIMENSION, DIMENSION])
            attributes = self.get_board_attributes(board)
            self.board = (board, attributes)
            if (not self.player_won(PLAYER_1)) and (not self.player_won(PLAYER_2)):
                break

    def get_board_attributes(self, board):
        connections_p1 = total_adjacents(board, PLAYER_1)
        aligned_p1 = max_aligned_pieces(board, PLAYER_1)
        components_p1 = total_components(board, PLAYER_1)
        connections_p2 = total_adjacents(board, PLAYER_2)
        aligned_p2 = max_aligned_pieces(board, PLAYER_2)
        components_p2 = total_components(board, PLAYER_2)

        return [connections_p1, aligned_p1, components_p1, connections_p2, aligned_p2, components_p2]

    def make_move(self, new_board):
        self.board = new_board

    # Returns new board with the piece moved
    def move_piece(self, current, future):
        if (is_valid_move(self.board[0], future)):
            future_board = deepcopy(self.board[0])
            future_board[future] = future_board[current]
            future_board[current] = FREE
            new_board = (future_board, self.get_board_attributes(future_board))
            return new_board
        return self.board[0]

    # Returns all the possible movement boards for a player
    def possible_moves(self, player):
        pieces = my_pieces(player, self.board[0])
        moves = []
        for mp in pieces:
            moves = moves + self.next_boards_for(mp)
        return moves

    # TODO: if one attribute takes diagonal pieces into account, this may be re written
    def player_won(self, turn):
        # Check horizontal positions
        for col in range(DIMENSION - 3):
            for row in range(DIMENSION):
                if self.board[0][row, col] == self.board[0][row, col+1] == self.board[0][row, col+2] == self.board[0][row, col+3] == turn:
                    return True

        # Check vertical positions
        for row in range(DIMENSION - 3):
            for col in range(DIMENSION):
                if self.board[0][row, col] == self.board[0][row+1, col] == self.board[0][row+2, col] == self.board[0][row+3, col] == turn:
                    return True

        # Check positiely sloped diagonals
        for row in range(DIMENSION - 3):
            for col in range(DIMENSION - 3):
                if self.board[0][row, col] == self.board[0][row+1, col+1] == self.board[0][row+2, col+2] == self.board[0][row+3, col+3] == turn:
                    return True

        # Check negativly sloped diagonals
        for row in range(3, DIMENSION):
            for col in range(3, DIMENSION - 3):
                if self.board[0][row, col] == self.board[0][row-1, col+1] == self.board[0][row-2, col+2] == self.board[0][row-3, col+3] == turn:
                    return True

        # Check for squares
        for col in range(DIMENSION - 1):
            for row in range(DIMENSION - 1):
                if self.board[0][row, col] == self.board[0][row, col+1] == self.board[0][row+1, col] == self.board[0][row+1, col+1] == turn:
                    return True

        return False

    # Returns list of possible movement positions for a piece
    def valid_moves_for(self, piece):
        adjacents = adjacent_positions(piece)
        res = []
        for ap in adjacents:
            if is_free(self.board[0], ap):
                res = res + [ap]
        return res

    def next_boards_for(self, piece):
        valid_moves = self.valid_moves_for(piece)
        next_boards = []
        for vm in valid_moves:
            next_boards = next_boards + [self.move_piece(piece, vm)]
        return next_boards
