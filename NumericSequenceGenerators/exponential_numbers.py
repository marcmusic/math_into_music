# Author: M.A.R.C Original Music
# ©2023
# Exponential Numbers Sequence Generator

# f(n) = n^2

def generate_sequence(num_of_terms = 10, exponent = 2) -> list[int]:
    return [pow(i+1, exponent) for i in range(num_of_terms)]

