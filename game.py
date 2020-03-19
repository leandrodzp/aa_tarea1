import numpy as np
from copy import deepcopy
from constants import DIMENSION, FREE, PLAYER_1, PLAYER_2
from helpers import my_pieces, adjacent_positions, adjacent_pieces, islands, is_valid_move, is_free

class Game(object):

  def __init__(self):
    while True: # Construct a non-winner board
      board = np.repeat(FREE, DIMENSION*DIMENSION)
      initial_positions = np.random.choice(25, 8, replace=False)
      board[initial_positions[0:4]] = PLAYER_1
      board[initial_positions[4:8]] = PLAYER_2
      board.resize([DIMENSION, DIMENSION])
      self.board = board
      if (not self.player_won(PLAYER_1)) and (not self.player_won(PLAYER_2)):
        break
  
  def make_move(self, new_board):
    # self.board = new_board
    pass

  # Returns new board with the piece moved
  def move_piece(self, current, future):
    if (is_valid_move(self.board, future)):
      future_board = deepcopy(self.board)
      future_board[future] = future_board[current]
      future_board[current] = FREE
    return future_board

  # Returns all the possible movement boards for a player
  def possible_moves(self, player):
    pieces = my_pieces(player, self.board)
    moves = []
    for mp in pieces:
      moves = moves + self.next_boards_for(mp)
    return moves

  def player_won(self, turn):
    # Check horizontal positions
    for col in range(DIMENSION - 3):
      for row in range(DIMENSION):
        if self.board[row,col] == self.board[row,col+1] == self.board[row,col+2] == self.board[row,col+3] == turn:
          return True

    # Check vertical positions
    for row in range(DIMENSION - 3):
      for col in range(DIMENSION):
        if self.board[row,col] == self.board[row+1,col] == self.board[row+2,col] == self.board[row+3,col] == turn:
          return True

    # Check positiely sloped diagonals
    for row in range(DIMENSION - 3):
      for col in range(DIMENSION - 3):
        if self.board[row,col] == self.board[row+1,col+1] == self.board[row+2,col+2] == self.board[row+3,col+3] == turn:
          return True

    # Check negativly sloped diagonals
    for row in range(3, DIMENSION):
      for col in range(3, DIMENSION - 3):
        if self.board[row,col] == self.board[row-1,col+1] == self.board[row-2,col+2] == self.board[row-3,col+3] == turn:
          return True

    # Check for squares
    for col in range(DIMENSION - 1):
      for row in range(DIMENSION - 1):
        if self.board[row,col] == self.board[row,col+1] == self.board[row+1,col] == self.board[row+1,col+1] == turn:
          return True

    return False

  # Returns list of possible movement positions for a piece
  def valid_moves_for(self, piece):
    adjacents = adjacent_positions(piece)
    res = []
    for ap in adjacents:
      if is_free(self.board, ap):
        res = res + [ap]
    return res

  def next_boards_for(self, piece):
    valid_moves = self.valid_moves_for(piece)
    next_boards = []
    for vm in valid_moves:
      next_boards = next_boards + [self.move_piece(piece, vm)]
    return next_boards

  def total_adjacents(self, player):
    pieces = my_pieces(player, self.board)
    total = 0
    for p in pieces:
      ap = adjacent_pieces(p, self.board)
      total += len(ap)
    return total

  def max_fichas_alineadas(self, player):
    pieces = my_pieces(player, self.board)
    pieces.sort()
    cant = 0

    # checks the largest current line
    for coord in pieces:
        if coord[0]+1 < DIMENSION and coord[1]+1 < DIMENSION and (coord[0]+1, coord[1]+1) in pieces: # right diagonal
            if coord[0]+2 < DIMENSION and coord[1]+2 < DIMENSION and (coord[0]+2, coord[1]+2) in pieces: # right diagonal
                if coord[0]+3 < DIMENSION and coord[1]+3 < DIMENSION and (coord[0]+3, coord[1]+3) in pieces: # right diagonal
                    return 4
                else:
                    return 3
            else:
                return 2
        if coord[0]+1 < DIMENSION and coord[1]-1 >= 0 and (coord[0]+1, coord[1]-1) in pieces: # left diagonal
            if coord[0]+2 < DIMENSION and coord[1]-2 >= 0 and (coord[0]+2, coord[1]-2) in pieces: # left diagonal
                if coord[0]+3 < DIMENSION and coord[1]-3 >= 0 and (coord[0]+3, coord[1]-3) in pieces: # left diagonal
                    return 4
                else:
                    return 3
            else:
                return 2
        if coord[1]+1 < DIMENSION and (coord[0], coord[1]+1) in pieces: # ->
            if coord[1]+2 < DIMENSION and (coord[0], coord[1]+2) in pieces: # -->
                if coord[1]+3 < DIMENSION and (coord[0], coord[1]+3) in pieces: # --->
                    return 4
                else:
                    return 3
            else:
                return 2
        if coord[0]+1 < DIMENSION and (coord[0]+1, coord[1]) in pieces: # downwards
            if coord[0]+2 < DIMENSION and (coord[0]+2, coord[1]) in pieces: # downwards
                if coord[0]+3 < DIMENSION and (coord[0]+3, coord[1]) in pieces: # downwards
                    return 4
                else:
                    return 3
            else:
                return 2
        # bandera para asegurar que evalue todas mis fichas.
        cant += 1
        if cant == 4:
            return 1
