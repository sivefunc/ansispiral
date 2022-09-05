from .up_direction import up_dir
from .down_direction import down_dir
from .left_direction import left_dir
from .right_direction import right_dir

make_direction = {
        'up': up_dir,
        'down': down_dir,
        'left': left_dir,
        'right': right_dir
        }

def num_spiral(rows, columns, downward=True):
    """
    return a NxM matrix containing the number spiral downward or upward
    """

    matrix = [[0] * columns for row in range(rows)] # 0 -> empty space
    number = rows * columns if downward else 1
    n_column, n_row = 0, 0
    direction = 'right'

    while not all([all(row) for row in matrix]): # not full
        number, n_column, n_row, direction = make_direction[direction](
                                            number, n_column,
                                            n_row, matrix, downward)

    return matrix
