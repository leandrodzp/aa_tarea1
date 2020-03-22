import sys
import click
from game import Game
from player import RandomPlayer, LearningPlayer
from constants import RANDOM, TRAIN, PLAYER_1, PLAYER_2, WIN, LOST, TIE

@click.command()
@click.option('--p2', default = 1, type = click.IntRange(1, 2), help='1 - Juegador aleatorio, \n 2 - Jugador inteligente')
@click.option('--qnty', default = 200, type = click.INT, help='Cantidad de partidos a jugar')
@click.option('--moves', default = 500, type = click.INT, help='Cantidad maxima de movimientos del partido')
@click.option('--learn', default = True, type = click.BOOL, help='True - El jugador 1 aprende\n False - El jugador 1 no aprende')

def main(p2, qnty, moves, learn):
    player1 = LearningPlayer(PLAYER_1, learn)

    if (p2 == 1):
        player2 = RandomPlayer(PLAYER_2)
    else:
        player2 = LearningPlayer(PLAYER_2, False)

    num_games = qnty
    max_moves = moves
    num_wins_p1 = 0
    num_wins_p2 = 0
    num_ties = 0

    for _ in range(num_games):
        winner = False
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
                winner = True
                player1.end_game(game.board, WIN if turn == PLAYER_1 else LOST)
                player2.end_game(game.board, WIN if turn == PLAYER_2 else LOST)
                if (turn == PLAYER_1): num_wins_p1 += 1
                if (turn == PLAYER_2): num_wins_p2 += 1
                break
            turn = PLAYER_1 if (turn == PLAYER_2) else PLAYER_2
            i += 1
        print('MOVES ', i)
        if (i == max_moves and not winner):
            print('ITS A TIE! ', turn)
            num_ties += 1
            player1.end_game(game.board, TIE)
            player2.end_game(game.board, TIE)

    print('winners p1 ', num_wins_p1)
    print('winners p2 ', num_wins_p2)
    print('ties ', num_ties)


if __name__ == "__main__":
    main()
