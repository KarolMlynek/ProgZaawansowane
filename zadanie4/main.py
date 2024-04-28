from random import randint
#black == 0 white == 1
def board_generator():
    board = []
    for i in range(8):
        arr = []
        for j in range(8):
            arr.append(randint(0,1))
        board.append(arr)
    return board
def show_board(board):
    for i in range(len(board)):
        print(board[i])
def Neighbor_count(board):
    rows = 8
    cols = 8
    counted_neighbors = [[0] * cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == 0:
                total_white_neighbors = 0
                total_black_neighbors = -1
            else:
                total_white_neighbors = -1
                total_black_neighbors =  0

            for di in range(-1, 2):
                for dj in range(-1, 2):
                    ni, nj = i + di, j + dj
                    if 0 <= ni < rows and 0 <= nj < cols:
                        if board[ni][nj] == 0:
                            total_black_neighbors += 1
                        else:
                            total_white_neighbors += 1
            if total_black_neighbors < 0:
                total_black_neighbors = 0
            elif total_white_neighbors < 0:
                total_white_neighbors = 0

            counted_neighbors[i][j] = f"black = {total_black_neighbors} and white = {total_white_neighbors}"

    return counted_neighbors
#generated_board = matrix = [[(i + j) % 2 for i in range(8)] for j in range(8)]
generated_board = board_generator()
print('SHOW BOARD:')
print(show_board(generated_board))
print('SHOW NEIGHBOURS')
print(show_board(Neighbor_count(generated_board)))


