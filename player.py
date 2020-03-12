from abc import ABC, abstractmethod
from constants import RANDOM, TRAIN
import numpy as np

class Player(ABC):
  def __init__(self, type = RANDOM):
    super().__init__
    self.type = type
  
  @abstractmethod
  def make_move():
    pass

class RandomPlayer(Player):

  def make_move(self, possible_moves):
    # next_move = np.random.choice(possible_moves, 1)
    next_move = []
    return next_move

class TrainPlayer(Player):
  def __init__(self):
    super().__init__

  def make_move(self, possible_moves):
    pass