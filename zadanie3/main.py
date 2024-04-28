from random import randint
n = randint(1,10)
def matrix_generator(n):
    matrix = []
    for i in range(n):
        arr = []
        for j in range(n):
            arr.append(randint(0,10))
        matrix.append(arr)
    return matrix

def matrix_smoother(generated_matrix):
    if len(generated_matrix) == 1:
        return generated_matrix
    rows = len(generated_matrix)
    cols = len(generated_matrix[0])
    smoothed_matrix = [[0] * cols for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            total_neighbors = 0
            total_sum = 0

            for di in range(-1, 2):
                for dj in range(-1, 2):
                    ni, nj = i + di, j + dj
                    if 0 <= ni < rows and 0 <= nj < cols:
                        total_sum += generated_matrix[ni][nj]
                        total_neighbors += 1

            smoothed_matrix[i][j] = round(total_sum / total_neighbors, 2)

    return smoothed_matrix
def matrix_displayer(smooth_matrix):
    for i in range(len(smooth_matrix)):
        print(smooth_matrix[i])
print(n)
#print(matrix_generator(n))
#print((matrix_smoother(matrix_generator(n))))
print(matrix_displayer(matrix_smoother(matrix_generator(n))))
