# Author: M.A.R.C Original Music
# ©2023

def generate_sequence(num_of_terms = 10) -> list[int]:
    sequence = [1,1]

    for i in range(2, num_of_terms):
        sequence.append(sequence[i-2] + sequence[-1])

    return sequence