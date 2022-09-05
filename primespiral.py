import copy
from spiral.number_spiral import num_spiral

def isprime(n):
    """
    return a boolean indicating the identity of the number
    """
    
    if n in {2, 3}:
        return True
    return all([n % i for i in range(2, n)])

def prime_spiral(rows, columns, downward=True):
    """
    return a NxM matrix spiral with just the prime numbers
    """

    spiral = num_spiral(rows, columns, downward)
    for Y, row in enumerate(copy.deepcopy(spiral)):
        for X, column in enumerate(row):
            if not isprime(column):
                spiral[Y][X] = 0
    return spiral
