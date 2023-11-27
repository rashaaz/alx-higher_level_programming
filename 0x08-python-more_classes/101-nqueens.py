#!/usr/bin/python3
"""N-Queens Solver"""

import sys


def in_b(n):
    """Initialize an empty chessboard of size n x n."""
    bo = []
    [bo.append([' ' for i in range(n)]) for i in range(n)]
    return bo


def bo_dee(bo):
    """Create a deep copy of the given 2D list."""
    if isinstance(bo, list):
        return list(map(bo_dee, bo))
    return bo


def print_solu(bo):
    """Print the coordinates of queens in the current solution."""
    solut = []
    for r in range(len(bo)):
        for c in range(len(bo)):
            if bo[r][c] == "Q":
                solut.append([r, c])
                break
    return solut


def mout(bo, row, col):
    """Mark the attacked positions on the board as 'x'

    Args:
        bo (list): The chessboard represented as a list of lists.
        row (int): The row index of the queen.
        col (int): The column index of the queen.
    """
    # x out
    for ss in range(col + 1, len(bo)):
        bo[row][ss] = "x"
    # x out all
    for ss in range(col - 1, -1, -1):
        bo[row][ss] = "x"
    # x out
    for sh in range(row + 1, len(bo)):
        bo[sh][col] = "x"
    # x out
    for sh in range(row - 1, -1, -1):
        bo[sh][col] = "x"
    # x out
    ss = col + 1
    for sh in range(row + 1, len(bo)):
        if ss >= len(bo):
            break
        bo[sh][ss] = "x"
        ss += 1
    # x out
    ss = col - 1
    for sh in range(row - 1, -1, -1):
        if ss < 0:
            break
        bo[sh][ss] = "x"
        ss -= 1
    # x out
    ss = col + 1
    for sh in range(row - 1, -1, -1):
        if ss >= len(bo):
            break
        bo[sh][ss] = "x"
        ss += 1
    # x out
    ss = col - 1
    for sh in range(row + 1, len(bo)):
        if ss < 0:
            break
        bo[sh][ss] = "x"
        ss -= 1


def rec_slov(bo, row, que, solut):
    """Recursively solve the N-Queens problem and find all solutions.

    Args:
        bo (list): The chessboard represented as a list of lists.
        row (int): The current row being considered.
        que (int): The number of queens placed on the board so far.
        solut (list): A list to store the solutions.

    Returns:
        list: A list of solutions.
    """
    if que == len(bo):
        solut.append(print_solu(bo))
        return solut

    for ss in range(len(bo)):
        if bo[row][ss] == " ":
            tp_bo = bo_dee(bo)
            tp_bo[row][ss] = "Q"
            mout(tp_bo, row, ss)
            solut = rec_slov(tp_bo, row + 1, que + 1, solut)
    return solut


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    bo = in_b(int(sys.argv[1]))
    solut = rec_slov(bo, 0, 0, [])
    for mol in solut:
        print(mol)
