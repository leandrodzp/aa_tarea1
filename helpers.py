def my_pieces(self, player):
  positions = np.where(self.board == player)
  positions = list(zip(positions[0],positions[1]))
  return positions

def valid_moves(self, piece):
  pass

def adyacent_positions(self, position):
  pass