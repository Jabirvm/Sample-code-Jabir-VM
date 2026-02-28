"""
Moving Window Bin Generator with Total Consistency Check

Parameters:
    T  → Total number of elements (Supernovae)
    n  → Number of elements per bin
    o  → Overlap between adjacent bins
    N  → Number of bins

Consistency condition:
    T = Nn - (N - 1)o
"""

def generate_bins(n, o, bins):
    start = 1
    shift = n - o
    bin_ranges = []

    for i in range(bins):
        bin_start = start + i * shift
        bin_end = bin_start + n - 1
        bin_ranges.append((bin_start, bin_end))

    return bin_ranges


def main():
    print("\n--- Moving Window Bin Generator ---\n")

    try:
        T = int(input("Enter total number of elements (T): "))
        n = int(input("Enter number of elements per bin (n): "))
        o = int(input("Enter overlap between bins (o): "))
        bins = int(input("Enter number of bins (N): "))

        if o >= n:
            raise ValueError("Overlap (o) must be smaller than n.")

        expected_T = bins * n - (bins - 1) * o

        if expected_T != T:
            raise ValueError(
                f"Inconsistent parameters.\n"
                f"Expected total = {expected_T}, but given T = {T}"
            )

        ranges = generate_bins(n, o, bins)

        print("\nParameters are consistent.")
        print("\nGenerated Bin Ranges:\n")

        for i, (low, high) in enumerate(ranges, 1):
            print(f"Bin {i}: ({low} - {high})")

    except ValueError as e:
        print(f"\nError: {e}")


if __name__ == "__main__":
    main()
