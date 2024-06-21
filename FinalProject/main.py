EMPTY = 0
BLACK = 1
WHITE = 2

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

def is_valid_move(board, player, row, col):
    if board[row][col] != EMPTY:
        return False

    opponent = WHITE if player == BLACK else BLACK
    for dr, dc in DIRECTIONS:
        r, c = row + dr, col + dc
        if 0 <= r < 8 and 0 <= c < 8 and board[r][c] == opponent:
            while 0 <= r < 8 and 0 <= c < 8:
                r += dr
                c += dc
                if not (0 <= r < 8 and 0 <= c < 8):
                    break
                if board[r][c] == EMPTY:
                    break
                if board[r][c] == player:
                    return True
    return False


def find_valid_moves(board, player):
    valid_moves = []
    for row in range(8):
        for col in range(8):
            if is_valid_move(board, player, row, col):
                valid_moves.append((row, col))
    return valid_moves

board = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 2, 1, 0, 0, 0],
    [0, 0, 0, 1, 2, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]


valid_moves_black = find_valid_moves(board, BLACK)
print("Legalne ruchy dla czarnego gracza:", valid_moves_black)


valid_moves_white = find_valid_moves(board, WHITE)
print("Legalne ruchy dla białego gracza:", valid_moves_white)
