# Author: M.A.R.C Original Music
# ©2023

def convert_int_to_sequence(num) -> list[int]:
    sequence = []
    while num > 0:
        sequence.insert(0, num % 10)
        num = num // 10

    return sequence