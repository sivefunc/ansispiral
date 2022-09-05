def down_dir(number, n_column, n_row, matrix, downward=True):
    """
    Modifies the NxM matrix in the left direction of the given row and
    column by putting the number upward or downward
    """
    
    # get the down border by finding the last empty spot of the ver. columns
    border = -(list(reversed([matrix[y][n_column] for y, r in enumerate(
                                            matrix)])).index(0)) + len(matrix)
    for row in range(n_row, border):
        matrix[row][n_column] = number
        if not all([matrix[y][n_column] for y, r in enumerate(matrix)]):
            number = number - 1 if downward else number + 1
    return number, n_column, row, 'left'
