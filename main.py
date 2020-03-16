from game import Game
from player import RandomPlayer
from constants import RANDOM, TRAIN, PLAYER_1, PLAYER_2


if __name__ == "__main__":
  turn = PLAYER_1
  game = Game()
  player1 = RandomPlayer(1)
  player2 = RandomPlayer(2)
  max_moves = 50
  i = 0
  while i < max_moves:
    all_moves = game.possible_moves(turn)
    if (turn == PLAYER_1):
      next_move = player1.make_move(all_moves)
    else:
      next_move = player2.make_move(all_moves)
    game.make_move(next_move)
    if (game.player_won(turn)):
      print('THE WINNER IS ', turn)
      break
    turn = PLAYER_1 if (turn == PLAYER_2) else PLAYER_2
    i += 1
