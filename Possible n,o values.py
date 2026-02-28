"""
Moving Window Analysis: Integer Solver for n and o

This script finds valid integer combinations of:
    n → Number of Supernovae per bin
    o → Overlap between adjacent bins

Equation used:
    o = ((n * N) - T) / (N - 1)
"""

def find_valid_combinations(T, N, min_n, max_n):
    """
    Find valid (n, o) integer pairs within a specified n range.

    Parameters
    ----------
    T : int
        Total number of Supernovae
    N : int
        Number of bins
    min_n : int
        Minimum value of n to test
    max_n : int
        Maximum value of n to test

    Returns
    -------
    list of tuples
        Valid (n, o) integer pairs
    """

    if N <= 1:
        raise ValueError("N must be greater than 1.")

    valid_combinations = []

    for n in range(min_n, max_n + 1):
        numerator = (n * N) - T
        denominator = (N - 1)

        # Check integer condition using modulus (safer than float .is_integer())
        if numerator % denominator == 0:
            o = numerator // denominator

            if o >= 0:
                valid_combinations.append((n, o))

    return valid_combinations


def main():
    T = 1829   # Number of SNe
    N = 10     # Number of bins

    min_n = 50
    max_n = 700

    solutions = find_valid_combinations(T, N, min_n, max_n)

    if solutions:
        print("\nPossible (n, o) values:")
        for n, o in solutions:
            print(f"n = {n}, o = {o}")
    else:
        print("\nNo valid (n, o) values found in the given range.")


if __name__ == "__main__":
    main()


