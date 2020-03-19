from game import Game
from player import RandomPlayer, LearningPlayer
from constants import RANDOM, TRAIN, PLAYER_1, PLAYER_2


if __name__ == "__main__":
    turn = PLAYER_1
    game = Game()
    player1 = LearningPlayer(PLAYER_1)
    player2 = RandomPlayer(PLAYER_2)
    max_moves = 500
    i = 0
    #TODO: TIE?
    while i < max_moves:
        all_moves = game.possible_moves(turn)
        print('TURN IS FOR PLAYER ', turn)
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        print('Its board is ', game.board[0])
        if (turn == PLAYER_1):
            next_move = player1.make_move(game.board, all_moves)
        else:
            next_move = player2.make_move(game.board, all_moves)
        game.make_move(next_move)
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        print('Next board is \n', game.board[0])
        if (game.player_won(turn)):
            player1.end_game(turn == PLAYER_1)
            player2.end_game(turn == PLAYER_2)
            print('THE WINNER IS ', turn)
            break
        turn = PLAYER_1 if (turn == PLAYER_2) else PLAYER_2
        i += 1
