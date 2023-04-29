# Author: M.A.R.C Original Music
# ©2023

class NumericSequence:
    def __init__(self, id, name, numeric_sequence, description) -> None:
        self.id = id
        self.name = name
        self.numeric_sequence = numeric_sequence
        self.description = description

    def __str__(self) -> str:
        return str(self.id) + "\n" + str(self.name) + "\n" + str(self.description) + "\n" + str(self.numeric_sequence)