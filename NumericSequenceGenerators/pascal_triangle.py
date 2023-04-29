# Author: M.A.R.C Original Music
# ©2023
# Pascal Triangle Sequence Generator

from .util.numeric_sequence import NumericSequence

def generate_sequence(num_of_levels = 10) -> NumericSequence:
    sequence = []
    for i in range(num_of_levels):
        sequence += generate_pascal_triangle_level_sequence(i)
    return NumericSequence('S-12-0002','Pascal Triangle', sequence, '1 \n1,1\n1,2,1.')


def generate_pascal_triangle_level_sequence(level_num):
    level_sequence = [1]
    for i in range(level_num):
        level_sequence.append(level_sequence[i] * (level_num-i) // (i+1))
    return level_sequence
    