import numpy as np
from copy import deepcopy
from constants import DIMENSION, FREE, PLAYER_0, PLAYER_1, ROW, COL
from helpers import my_pieces, valid_moves, adyacent_positions
class Game(object):

  def __init__(self):
    while True: # Construct a non-winner board
      board = np.repeat(FREE, DIMENSION*DIMENSION)
      initial_positions = np.random.choice(25, 8, replace=False)
      board[initial_positions[0:4]] = PLAYER_0
      board[initial_positions[4:8]] = PLAYER_1
      board.resize([DIMENSION, DIMENSION])
      self.board = board
      if (not self.player_won(PLAYER_0)) and (not self.player_won(PLAYER_1)):
        break
    
    self.status = 'playing'

  # def move_piece(self, current, future):
  #   if (self.is_valid_move(future)):
  #     self.board[future] = self.board[current]
  #     self.board[current] = FREE

  def move_piece(self, new_board):
    self.board = new_board

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


