import numpy as np


piece_to_value = {
    'P': 1,  'N': 3,  'B': 3,  'R': 5,  'Q': 9,  'K': 100,
    'p': -1, 'n': -3, 'b': -3, 'r': -5, 'q': -9, 'k': -100,
    '': 0  # empty square
}

def init_board():
    # Create an empty board
    board_str = np.full(shape=(8, 8),fill_value='', dtype=object)

    # Set up black pieces
    board_str[0] = ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']
    board_str[1] = ['p'] * 8

    # Set up white pieces
    board_str[6] = ['P'] * 8
    board_str[7] = ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']

    board_int = np.vectorize(lambda p: piece_to_value.get(p, 0))(board_str)
    return board_str , board_int



# define the state of the board
# move a piece , capture a piece , en passent , castle



if __name__ == '__main__':
    board_str = init_board()
    board_int = np.vectorize(lambda p: piece_to_value.get(p, 0))(board_str)

    print(board_str,board_int)