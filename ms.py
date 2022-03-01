#  PUT YOUR NAME ANS UMBC ID HERE

from constraint import *
import timeout_decorator
import time

@timeout_decorator.timeout(30) # throw exception after 30 seconds
def ms(n, magic_sum=None, solver=BacktrackingSolver()):
    """ Solve a magic squares problem for a nxn grid and given
    magic_sum or computing a default magic sum if none is given using
    the given solver """

    pass


def ms_sizes(sizes):
    """ show time to solve magic square problems of varying sizes using different solvers. """
    solvers = [BacktrackingSolver, RecursiveBacktrackingSolver, MinConflictsSolver]
    for n in sizes:
        print(f"\nSize: {n}x{n}\n")
        for s in solvers:
            start_time = time.time()
            try:
                solution =  ms(n, magic_sum=None, solver=s())
            except timeout_decorator.TimeoutError:
                # ms function timed out
                solution = "timeout"
            except:
                # an unexpected error, raise to show to user.
                raise
            elapsed = time.time() - start_time
            print(f"{s.__name__}: {solution}; time:{elapsed:.3f}")

if __name__ == "__main__":
    ms_sizes(range(3,7))
