from game import Game
from player import RandomPlayer, LearningPlayer
from constants import RANDOM, TRAIN, PLAYER_1, PLAYER_2, WIN, LOST, TIE


if __name__ == "__main__":
    player1 = LearningPlayer(PLAYER_1)
    player2 = RandomPlayer(PLAYER_2)
    num_games = 500
    num_wins_p1 = 0
    num_wins_p2 = 0
    num_ties = 0

    for j in range(num_games):
        max_moves = 500
        i = 0
        turn = PLAYER_1
        game = Game()
        while i < max_moves:
            all_moves = game.possible_moves(turn)
            if (turn == PLAYER_1):
                next_move = player1.make_move(game.board, all_moves)
            else:
                next_move = player2.make_move(game.board, all_moves)
            game.make_move(next_move)
            if (game.player_won(turn)):
                player1.end_game(WIN if turn == PLAYER_1 else LOST)
                if (turn == PLAYER_1): num_wins_p1 += 1
                player2.end_game(WIN if turn == PLAYER_2 else LOST)
                if (turn == PLAYER_2): num_wins_p2 += 1
                print('THE WINNER IS ', turn)
                break
            turn = PLAYER_1 if (turn == PLAYER_2) else PLAYER_2
            i += 1
        print('MOVES ', i)
        if (i == max_moves):
            print('ITS A TIE! ', turn)
            num_ties += 1
            player1.end_game(TIE)
            player2.end_game(TIE)

    print('winners p1 ', num_wins_p1)
    print('winners p2 ', num_wins_p2)
    print('ties ', num_ties)

