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
  # TODO: TIE?
  # TODO: CHANGE BOARD REPRESENTATION (THE CODE ISNT WORKING BECAUSE OF THIS)
  # TODO: GET BOARD ATTRIBUTES
  while i < max_moves:
    all_moves = game.possible_moves(turn)
      next_move = player1.make_move(game.board, all_moves)
    else:
      next_move = player2.make_move(game.board, all_moves)
    game.make_move(next_move)
    if (game.player_won(turn)):
      player1.end_game(turn == PLAYER_1)
      player2.end_game(turn == PLAYER_2)
      print('THE WINNER IS ', turn)
      break
    turn = PLAYER_1 if (turn == PLAYER_2) else PLAYER_2
    i += 1
