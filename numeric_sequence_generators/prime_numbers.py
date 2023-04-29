# Author: M.A.R.C Original Music
# ©2023
# Prime Numbers Sequence Generator

from .util.numeric_sequence import NumericSequence

sequence = [2]

def generate_sequence(num_of_terms = 10) -> NumericSequence:
    next_natural_number = sequence[-1] + 1

    for i in range(len(sequence), num_of_terms):
        while not is_prime(next_natural_number):
            next_natural_number += 1
        sequence.append(next_natural_number)
        next_natural_number += 1

    return NumericSequence('S-23-0001','Prime Numbers', sequence, 'A natural number greater than 1 that is not a product of two smaller natural numbers.')

def is_prime(num) -> bool:
    for i in range (2, num // 2 + 1):
        if num % i == 0:
            return False
    return True