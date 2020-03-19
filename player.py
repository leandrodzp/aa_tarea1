import numpy as np
from abc import ABC, abstractmethod
from constants import RANDOM, TRAIN, W0, W1, W2, W3, W4, W5, W6, MU
from helpers import my_pieces


class Player(ABC):
    def __init__(self, num_player):
        super().__init__
        self.num_player = num_player

    @abstractmethod
    def make_move(self, current_board, possible_moves):
        
        pass

    @abstractmethod
    def end_game(self, winner):
        pass


class RandomPlayer(Player):
    def __init__(self, num_player):
        super().__init__(num_player)

    def make_move(self, current_board, possible_moves):
        next_move = np.random.choice(len(possible_moves), 1)
        return possible_moves[next_move[0]]

    def end_game(self, winner):
        pass


class LearningPlayer(Player):
    def __init__(self, num_player):
        super().__init__(num_player)
        self.moves = []
        self.weights = [W0, W1, W2, W3, W4, W5, W6]

    def eval_board(self, board):
        terms = board[1].copy()
        terms.insert(0, 1)
        res = np.dot(self.weights, terms)
        return res/(1 + abs(res))

    def create_train_examples(self, winner):
        train_examples = []
        for i, board in enumerate(self.moves):
            if (i < len(self.moves) - 1):
                example = (board, self.eval_board(self.moves[i + 1]))
                train_examples.append(example)

        train_examples.append((self.moves[-1], 1 if winner else -1))

        return train_examples

    def adjust_weights(self, winner):
        train_examples = self.create_train_examples(winner)

        for board, v_train in enumerate(train_examples):
            v_op = self.eval_board(board)

            for index, _ in enumerate(self.weights):
                self.weights[index] = MU * (v_train - v_op) * board[1][index]

    def make_move(self, current_board, possible_moves):
        val_best_move = -1
        best_boards = []
        for board in possible_moves:
            new_eval = self.eval_board(board)
            if (new_eval > val_best_move):
                best_boards = [board]
                val_best_move = new_eval
            if (new_eval == val_best_move):
                best_boards.append(board)
        next_board_index = np.random.choice(len(best_boards), 1)
        next_board = best_boards[next_board_index[0]]
        self.moves.extend([current_board, next_board])
        return next_board

    def end_game(self, winner):
        self.adjust_weights(winner)
        self.moves = []
