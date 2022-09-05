from sys import stdout
from os import get_terminal_size as terminal_size

from parser import parser
from primespiral import prime_spiral
from pandas import DataFrame

args = parser()
write = stdout.write

ESC = chr(27)
CSI = ESC + '['

def main():
    columns, rows = terminal_size() if args.fill else (args.columns, args.rows)
    spiral = prime_spiral(rows, columns, args.downward)
    
    if args.shownum:
        spaces = len(str(max([max(row) for row in spiral])))

    for row in spiral:
        for prime in row:
            if args.shownum:
                write(str(prime).center(spaces) + '  ')
            
            else:
                write(f'{CSI}40m ') if prime else write(f'{CSI}47m ')
        write('\n')

if __name__ == '__main__':
    try:
        
        main()
    
    finally:
        write(f'{CSI}0m')
