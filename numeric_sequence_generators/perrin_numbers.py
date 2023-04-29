# Author: M.A.R.C Original Music
# ©2023
# Perrin Sequence Generator

# f(0) = 3, f(1) = 0, f(2) = 2, f(n) = f(n-2) + f(n-3)

from .util.numeric_sequence import NumericSequence

def generate_sequence(num_of_terms = 10) -> NumericSequence:
    sequence = [3,0,2]

    for i in range(len(sequence), num_of_terms):
        sequence.append(sequence[i-2] + sequence[i-3])

    return NumericSequence('Perrin','Perrin numbers [1,1]', sequence, 'f(0) = 3, f(1) = 0, f(2) = 2, f(n) = f(n-2) + f(n-3) for n > 2.')