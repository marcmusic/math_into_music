# Author: M.A.R.C Original Music
# ©2023

def generate_sequence(num_of_levels = 10) -> list[int]:
    sequence = []
    for i in range(num_of_levels):
        sequence += generate_pascal_triangle_level_sequence(i)
    return sequence


def generate_pascal_triangle_level_sequence(level_num):
    level_sequence = [1]
    for i in range(level_num):
        level_sequence.append(level_sequence[i] * (level_num-i) // (i+1))
    return level_sequence
    