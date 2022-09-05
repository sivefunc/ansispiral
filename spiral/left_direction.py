def left_dir(number, n_column, n_row, matrix, downward=True):
    """
    Modifies the NxM matrix in the left direction of the given row and
    column by putting the number upward or downward
    """
    
    # get the left border by finding the first empty spot of the hor. row
    border = matrix[n_row].index(0) - 1
    for column in range(n_column, border, -1):
        matrix[n_row][column] = number
        if not all(matrix[n_row]):
            number = number - 1 if downward else number + 1
    return number, column, n_row, 'up'
