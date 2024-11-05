'''
Rules of Conway's Game of Life

The universe of the Game of Life is an infinite two-dimensional orthogonal grid of square cells, 
each of which is in one of two possible states, alive or dead, or "populated" or "unpopulated". 
Every cell interacts with its eight neighbours, which are the cells that are horizontally, vertically, 
or diagonally adjacent. At each step in time, the following transitions occur:

- Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.
- Any live cell with two or three live neighbours lives on to the next generation.
- Any live cell with more than three live neighbours dies, as if by overpopulation.
- Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

The initial pattern constitutes the seed of the system. The first generation is created by applying the 
above rules simultaneously to every cell in the seed—births and deaths occur simultaneously, and the discrete 
moment at which this happens is sometimes called a tick (in other words, each generation is a pure function 
of the preceding one). The rules continue to be applied repeatedly to create further generations.
'''

'''
Implementation method:

- Have a matrix with values of 0 or 1
- If 0, then print ' '
- If 1, then print '•'
'''

import random, time, copy



#-- CONSTANTS --#

SEED = 42       # Seed

N = 10           # Number of rows
C = 50           # Number of columns

DEAD = 0        # Value for Dead cells
ALIVE = 1       # Value for Living cells

DELAY = 0.05    # Value for the delay (in seconds)



#-- AUXILIAR FUNCTIONS --#

def number_of_neighbours(matrix, i, j):
    num_neighbours = 0
    
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),           (0, 1),
                  (1, -1),  (1, 0),  (1, 1)]
    
    for dr, dc in directions:
        ni, nj = i + dr, j + dc
        if 0 <= ni < N and 0 <= nj < C:
            if matrix[ni][nj] == 1:
                num_neighbours += 1

    return num_neighbours


def liveability_cell(cell, nn):
    if cell == ALIVE:
        if nn < 2 or nn > 3:
            return DEAD
        else:
            return ALIVE
    else:
        if nn == 3:
            return ALIVE
        return DEAD



#-- MAIN FUNCTIONS --#

def next_generation(matrix):
    for i in range(N):
        for j in range(C):
            num_neighbours = number_of_neighbours(matrix, i, j)
            matrix[i][j] = liveability_cell(matrix[i][j], num_neighbours)
    return matrix


def print_cells(matrix):
    matrix_chars=""
    for i in range(N):
        line = ""

        for j in range(C):
            line += "•" if matrix[i][j] else " "

        matrix_chars += line + ("\n" if i < N else "")

    print()
    print(matrix_chars, end='', flush=True)



#-- main() --#

if __name__ == "__main__":

    random.seed(SEED)
    matrix = [[random.randint(0, 2) for _ in range(C)] for _ in range(N)]
    previous_matrix = copy.deepcopy(matrix)

    while(1):
        matrix = next_generation(matrix)
        print_cells(matrix)
        
        time.sleep(DELAY)

        if previous_matrix == matrix:
            break
        else:
            previous_matrix = copy.deepcopy(matrix)
            print("\033[F" * (N+1), end='')

