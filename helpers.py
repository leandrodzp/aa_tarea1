import numpy as np
from constants import DIMENSION, FREE, ROW, COL

# Returns if number is in rage


def is_in_range(num):
    return (0 <= num <= DIMENSION - 1)

# Returns if a postion in board is free


def is_free(board, position):
    return (board[position] == FREE)

# Returns if moving a piece in a position is valid


def is_valid_move(board, position):
    return (is_in_range(position[ROW]) and is_in_range(position[COL]) and is_free(board, position))

# Returns list of the position of all the pieces of the player in the board


def my_pieces(player, board):
    positions = np.where(board == player)
    positions = list(zip(positions[0], positions[1]))
    return positions

# Returns distance between two pieces


def distance(piece1, piece2):
    subtract = (abs(piece1[0] - piece2[0]), abs(piece1[1] - piece2[1]))
    subtract = (subtract[0] - 1 if subtract[0] > 0 else 0,
                subtract[1] - 1 if subtract[1] > 1 else 0)
    return max(subtract)

# Returns list of all the adjacent positions of one piece


def adjacent_positions(position):
    row, col = position
    adjacents = [(row-1, col-1), (row-1, col), (row-1, col+1), (row, col+1),
                (row+1, col+1), (row+1, col), (row+1, col-1), (row, col-1)]
    adjacents = list(filter(lambda x: (x[0] >= 0 and x[1] >= 0) and (
        x[0] < DIMENSION and x[1] < DIMENSION), adjacents))
    return adjacents

# Return list of the adjacent pieces of one piece in a board


def adjacent_pieces(piece, board):
    player = board[piece]
    ap = adjacent_positions(piece)
    return list(filter(lambda x: (board[x] == player), ap))


def islands_helper(piece, board):
    visited = set()
    visited.add(piece)
    queue = [piece]
    while queue:
        actual = queue.pop()
        adjacents = adjacent_pieces(actual, board)
        for ad in adjacents:
            if not ad in visited:
                visited.add(ad)
                queue.append(ad)
    return visited

# Return list of islands of pieces of a player


def islands(player, board):
    pieces = set(my_pieces(player, board))
    res = []
    while pieces:
        piece = pieces.pop()
        component = islands_helper(piece, board)
        pieces = pieces - component
        res.append(list(component))
    return res


# Returns total components of the pieces in a board related to a player
def total_components(board, player):
    return len(islands(player, board))


def max_aligned_pieces(board, player):
    pieces = my_pieces(player, board)
    pieces.sort()
    cant = 0

    # checks the largest current line
    for coord in pieces:
        # right diagonal
        if coord[0]+1 < DIMENSION and coord[1]+1 < DIMENSION and (coord[0]+1, coord[1]+1) in pieces:
            # right diagonal
            if coord[0]+2 < DIMENSION and coord[1]+2 < DIMENSION and (coord[0]+2, coord[1]+2) in pieces:
                # right diagonal
                if coord[0]+3 < DIMENSION and coord[1]+3 < DIMENSION and (coord[0]+3, coord[1]+3) in pieces:
                    return 4
                else:
                    return 3
            else:
                return 2
        # left diagonal
        if coord[0]+1 < DIMENSION and coord[1]-1 >= 0 and (coord[0]+1, coord[1]-1) in pieces:
            # left diagonal
            if coord[0]+2 < DIMENSION and coord[1]-2 >= 0 and (coord[0]+2, coord[1]-2) in pieces:
                # left diagonal
                if coord[0]+3 < DIMENSION and coord[1]-3 >= 0 and (coord[0]+3, coord[1]-3) in pieces:
                    return 4
                else:
                    return 3
            else:
                return 2
        if coord[1]+1 < DIMENSION and (coord[0], coord[1]+1) in pieces:  # ->
            if coord[1]+2 < DIMENSION and (coord[0], coord[1]+2) in pieces:  # -->
                if coord[1]+3 < DIMENSION and (coord[0], coord[1]+3) in pieces:  # --->
                    return 4
                else:
                    return 3
            else:
                return 2
        if coord[0]+1 < DIMENSION and (coord[0]+1, coord[1]) in pieces:  # downwards
            if coord[0]+2 < DIMENSION and (coord[0]+2, coord[1]) in pieces:  # downwards
                # downwards
                if coord[0]+3 < DIMENSION and (coord[0]+3, coord[1]) in pieces:
                    return 4
                else:
                    return 3
            else:
                return 2
        # bandera para asegurar que evalue todas mis fichas.
        cant += 1
        if cant == 4:
            return 1

def total_adjacents(board, player):
    pieces = my_pieces(player, board)
    total = 0
    for p in pieces:
        ap = adjacent_pieces(p, board)
        total += len(ap)
    return total
