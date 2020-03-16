import numpy as np
from abc import ABC, abstractmethod
from constants import RANDOM, TRAIN, W0, W1, W2, W3, W4, W5, W6
from helpers import my_pieces

class Player(ABC):
  def __init__(self, num_player):
    super().__init__
    self.num_player = num_player
  
  @abstractmethod
  def make_move():
    pass

class RandomPlayer(Player):
  def __init__(self, num_player):
    super().__init__(num_player)

  def make_move(self, possible_moves):
    # next_move = np.random.choice(possible_moves, 1)
    next_move = []
    return next_move

class LearningPlayer(Player):
  def __init__(self, num_player):
    super().__init__(num_player)
    self.moves = []
    self.weights = [W0, W1, W2, W3, W4, W5, W6]
  
  def eval_board(self, board):
    # TODO 
    # terms = self.get_board_attributes(board)
    # terms.insert(0, 1)
    # trans_terms = np.array(terms)
    # trans_terms.transpose()
    # weights = np.array(self.weights)
    # res = 
    return 3

  def adjust_weights(self):
    pass
  
  # Returns the attributes asociated with a board and a player
  def get_board_attributes(self, board):
    return [1, 2, 3, 4, 5, 6]

  def make_move(self, possible_moves):
    val_best_move = -1
    best_boards = []
    for board in possible_moves:
      new_eval = self.eval_board(board)
      if (new_eval > val_best_move):
        best_boards = [board]
        val_best_move = new_eval
      if (new_eval == val_best_move):
        best_boards.append(board)
    next_board = np.random.choice(best_boards, 1)
    moves = self.moves
    moves.append(next_board)
    self.moves = moves
    return next_board
