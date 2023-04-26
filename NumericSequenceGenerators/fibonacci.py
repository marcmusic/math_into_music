# Author: M.A.R.C Original Music
# ©2023

# f(0) = 1, f(0) = 1, f(n) = f(n-1) + f(n-1)

def generate_sequence(num_of_terms = 10) -> list[int]:
    sequence = [1,1]

    for i in range(len(sequence), num_of_terms):
        sequence.append(sequence[i-1] + sequence[i-2])

    return sequence