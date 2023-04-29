# Author: M.A.R.C Original Music
# ©2023
# Fibonacci Sequence Generator

# f(0) = 1, f(0) = 1, f(n) = f(n-1) + f(n-1)

from .util.numeric_sequence import NumericSequence

def generate_sequence(num_of_terms = 10) -> NumericSequence:
    sequence = [1,1]

    for i in range(len(sequence), num_of_terms):
        sequence.append(sequence[i-1] + sequence[i-2])

    return NumericSequence('S-12-0001','Fibonacci [1,1]', sequence, 'f(0) = 1, f(1) = 1, f(n) = f(n-1) + f(n-2)')