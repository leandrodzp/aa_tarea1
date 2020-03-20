import numpy as np
from abc import ABC, abstractmethod
from constants import RANDOM, TRAIN, W0, W1, W2, W3, W4, W5, W6, MU, WIN, LOST, TIE
from helpers import my_pieces


class Player(ABC):
    def __init__(self, num_player):
        super().__init__
        self.num_player = num_player

    @abstractmethod
    def make_move(self, current_board, possible_moves):
        
        pass

    @abstractmethod
    def end_game(self, result):
        pass


class RandomPlayer(Player):
    def __init__(self, num_player):
        super().__init__(num_player)

    def make_move(self, current_board, possible_moves):
        next_move = np.random.choice(len(possible_moves), 1)
        return possible_moves[next_move[0]]

    def end_game(self, result):
        pass


class LearningPlayer(Player):
    def __init__(self, num_player):
        super().__init__(num_player)
        self.moves = []
        self.weights = [W0, W1, W2, W3, W4, W5, W6]

    def eval_board(self, board):
        terms = board[1].copy()
        terms.append(1)
        res = np.dot(self.weights, terms)
        return res/(1 + abs(res))
    
    def eval_final(self, result):
        if (result == WIN): return 1
        if (result == LOST): return -1
        if (result == TIE): return -0.5

    def create_train_examples(self, result):
        train_examples = []
        for i, board in enumerate(self.moves):
            if (i < len(self.moves) - 1):
                example = (board, self.eval_board(self.moves[i + 1]))
                train_examples.append(example)
        result_final = self.eval_final(result)
        train_examples.append((self.moves[-1], result_final))

        return train_examples

    def adjust_weights(self, result):
        train_examples = self.create_train_examples(result)

        for board, v_train in train_examples:
            v_op = self.eval_board(board)

            for index, _ in enumerate(self.weights):
                coeficient = 1 if index == len(self.weights) - 1 else board[1][index]
                self.weights[index] = MU * (v_train - v_op) * coeficient

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

    def end_game(self, result):
        self.adjust_weights(result)
        print('The weights ', self.weights)
        self.moves = []
