# Author: M.A.R.C Original Music
# ©2023

# f(0) = 3, f(1) = 0, f(2) = 2, f(n) = f(n-2) + f(n-3)

def generate_sequence(num_of_terms = 10) -> list[int]:
    sequence = [3,0,2]

    for i in range(len(sequence), num_of_terms):
        sequence.append(sequence[i-2] + sequence[i-3])

    return sequence