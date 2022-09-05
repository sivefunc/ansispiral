def right_dir(number, n_column, n_row, matrix, downward=True):
    """
    Modifies the NxM matrix in the right direction of the given row and
    column by putting the number upward or downward
    """
    
    # get the right border by finding the last empty spot of the hor. row
    border = -(list(reversed(matrix[n_row])).index(0)) + len(matrix[n_row])
    for column in range(n_column, border):
        matrix[n_row][column] = number
        if not all(matrix[n_row]):
            number = number - 1 if downward else number + 1
    return number, column, n_row, 'down'
