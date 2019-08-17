"""
Given a chain of matrices (assume that they are compatible in terms of
multiplication), in what order should you multiply the matrices,
such that the cost of multiplying is minimized.

Return only the min cost of multiplying, no need to trace back.

eg. A B C D can be computed as (AB)(BC), (((AB)C)D), ... many ways to
do this
"""


def costOfMultiplying(A, B):
    return A[0] * B[1] * A[1]
