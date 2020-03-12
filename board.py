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
    while True: # Construct a non-winner board
      board = np.repeat(FREE,DIMENSION*DIMENSION)
      initial_positions = np.random.choice(25, 8, replace=False)
      board[initial_positions[0:4]] = PLAYER_0
      board[initial_positions[4:8]] = PLAYER_1
      board.resize([5,5])
      self.board = board
      if (not self.player_won(PLAYER_0)) and (not self.player_won(PLAYER_1)):
        break
    
    self.status = 'playing'

  def move_piece(self, current, future):
    if (self.is_valid_move(future)):
      self.board[future] = self.board[current]
      self.board[current] = FREE

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



##################### MOVEMENT VALIDATIONS ###################

  def is_valid_move(self, position):
    return (self.is_in_range(position[ROW]) and self.is_in_range(position[COL]) and self.is_free(position))

  def is_in_range(self, num):
    return (0 <= num <= DIMENSION - 1)
  
  def is_free(self, position):
    return (self.board[position] == FREE)

##################### USEFUL FUNCTIONS #####################

  def my_pieces(self, player):
    positions = np.where(self.board == player)
    positions = list(zip(positions[0],positions[1]))
    return positions

  def valid_moves(self, piece):
    pass

  def adyacent_positions(self, position):
    pass
