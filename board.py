import numpy as np
from copy import deepcopy

DIMENSION = 5
FREE = -1
PLAYER_0 = 0
PLAYER_1 = 1
ROW = 0
COL = 1

class Board(object):

  def __init__(self):
    self.board = np.zeros((DIMENSION,DIMENSION))
    self.board.fill(FREE)
    self.status = 'playing'

  def move_piece(self, current, future):
    if (self.is_valid_move(future)):
      self.board[future] = self.board[current]
      self.board[current] = FREE

  def winning_move(self, turn):
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

      return False



##################### MOVEMENT VALIDATIONS ###################

  def is_valid_move(self, position):
    return (self.is_in_range(position[ROW]) and self.is_in_range(position[COL]) and self.is_free(position))

  def is_in_range(self, num):
    return (0 <= num <= DIMENSION - 1)
  
  def is_free(self, position):
    return (self.board[position] == FREE)
