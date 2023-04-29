# Author: M.A.R.C Original Music
# ©2023
# Exponential Numbers Sequence Generator

# f(n) = n^^2

from .util.numeric_sequence import NumericSequence

def generate_sequence(num_of_terms = 10, exponent = 2) -> NumericSequence:
    sequence =  [pow(i+1, exponent) for i in range(num_of_terms)]
    return NumericSequence(f'Exponential-{exponent}',f'Exponential Numbers n^^{exponent}', sequence, f'f(n) = n^^{exponent}')

