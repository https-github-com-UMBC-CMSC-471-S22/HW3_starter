"""
Complete the ms() program so that it will try to find a magic square
of of size n using a CSP solver.  

You will need to install two packages with pip: python-constraint and
wrapt-timeout-decorator. On gl, you can install packages using the
user flag:

  pip install --user python-constraint
  pip install --user wrapt-timeout-decorator
"""

#  PUT YOUR NAME AND UMBC ID HERE

import constraint as c
import wrapt_timeout_decorator as t
import time

@t.timeout(30)     # throw exception after 30 seconds
def ms(n=3, magic_sum=None, solver=c.BacktrackingSolver()):
    """ Solve a magic squares problem for a nxn grid and given
    magic_sum or computing a default magic sum if none is given using
    the given solver """

    pass

def ms_sizes(sizes):
    """ show time to solve magic square problems of varying sizes using different solvers. """
    solvers = [c.BacktrackingSolver, c.RecursiveBacktrackingSolver, c.MinConflictsSolver]
    for n in sizes:
        print(f"\nSize: {n}x{n}\n")
        for s in solvers:
            start_time = time.time()
            try:
                solution =  ms(n, magic_sum=None, solver=s())
            except OSError:
                # ms function timed out
                solution = "timeout"
            except:
                # an unexpected error, raise to show to user.
                raise
            elapsed = time.time() - start_time
            print(f"{s.__name__}: {solution}; time:{elapsed:.3f}")

if __name__ == "__main__":
    ms_sizes(range(3,6))
