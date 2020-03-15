import numpy as np

def my_pieces(player, board):
  positions = np.where(board == player)
  positions = list(zip(positions[0],positions[1]))
  return positions

def distance(piece1, piece2):
  subtract = (abs(piece1[0] - piece2[0]), abs(piece1[1] - piece2[1]))
  subtract = (subtract[0] - 1 if subtract[0] > 0 else 0, subtract[1] - 1 if subtract[1] > 1 else 0)
  return max(subtract)