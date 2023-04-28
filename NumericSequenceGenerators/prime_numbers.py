# Author: M.A.R.C Original Music
# ©2023
# Prime Numbers Sequence Generator

sequence = [2]

def generate_sequence(num_of_terms = 10) -> list[int]:
    next_natural_number = sequence[-1] + 1

    for i in range(len(sequence), num_of_terms):
        while not is_prime(next_natural_number):
            next_natural_number += 1
        sequence.append(next_natural_number)
        next_natural_number += 1

    return sequence

def is_prime(num) -> bool:
    for i in range (2, num // 2 + 1):
        if num % i == 0:
            return False
    return True