import argparse

def parser():
    parser = argparse.ArgumentParser(
            prog="AnsiSpiral",
            formatter_class=argparse.RawDescriptionHelpFormatter,
            description="Simple prime spiral viewer")

    parser.add_argument(
            '-v','--version',
            action='version',
            version="""
%(prog)s v1.0.0
Copyright (C) 2022 Sivefunc
License GPLv3+: GNU GPL version 3 or later <https://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

Written by a human""")

    parser.add_argument(
            '-r', '--rows', 
            type=int,
            default=10,
            help='rows of NxM prime spiral',
            metavar="")
 
    parser.add_argument(
            '-c', '--columns', 
            type=int,
            default=10,
            help='columns of NxM prime spiral',
            metavar="")

    parser.add_argument(
            '-f', '--fill', 
            action="store_true",
            help='NxM prime spiral size the same as terminal screen')

    parser.add_argument(
            '-dw', '--downward', 
            action="store_false",
            help="NxM prime spiral numbers won't be downward")
    
    args = parser.parse_args()
    return args
