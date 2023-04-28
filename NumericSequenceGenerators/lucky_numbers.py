# Author: M.A.R.C Original Music
# ©2023
# Lucky Numbers Generator
# A000959 - https://oeis.org/A000959

def generate_sequence(num_of_terms = 10) -> list[int]:
    elimination_sequence = []
    sequence = seed_sequence(num_of_terms * 23)
    iteration = 1
    elimination_step = 2

    while iteration < len(sequence) - 1:
        for index, num in enumerate(sequence, start=1):
            if index % elimination_step == 0:
                elimination_sequence.append(num)

        sequence = [i for i in sequence if i not in elimination_sequence]
        elimination_step = sequence[iteration]
        iteration += 1
        elimination_sequence = []

    return sequence

def seed_sequence(num_of_terms) -> list[int]:
    seed = []
    for i in range(num_of_terms):
        seed.append(i + 1)

    return seed
