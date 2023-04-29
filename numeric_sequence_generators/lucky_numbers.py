# Author: M.A.R.C Original Music
# ©2023
# Lucky Numbers Sequence Generator

from .util.numeric_sequence import NumericSequence

def generate_sequence(num_of_terms = 10) -> NumericSequence:
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

    return NumericSequence('Lucky','Lucky Numbers', sequence, 'Add description')

def seed_sequence(num_of_terms) -> list[int]:
    seed = []
    for i in range(num_of_terms):
        seed.append(i + 1)

    return seed
