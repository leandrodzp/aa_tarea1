import numpy as np
from abc import ABC, abstractmethod
from constants import RANDOM, TRAIN
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
    self.weights = []
  
  def eval_board(self, board):

    return 3

  def adjust_weights(self):
    pass

  def make_move(self, possible_moves):
    val_best_move = -1
    for board in possible_moves:
      new_eval = self.eval_board(board)
      if (new_eval > val_best_move):
        best_board = board
        val_best_move = new_eval
    self.moves.append(best_board)
    return best_board
