def up_dir(number, n_column, n_row, matrix, downward=True):
    """
    Modifies the NxM matrix in the up direction of the given row and
    column by putting the number upward or downward
    """

    # get the up border by finding the first empty spot of the ver. columns
    border = [matrix[y][n_column] for y, r in enumerate(matrix)].index(0) - 1
    for row in range(n_row, border, -1):
        matrix[row][n_column] = number
        if not all([matrix[y][n_column] for y, r in enumerate(matrix)]):
            number = number - 1 if downward else number + 1
    return number, n_column, row, 'right'
