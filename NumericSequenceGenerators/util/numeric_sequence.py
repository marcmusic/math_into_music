class NumericSequence:
    def __init__(self, id, name, numeric_sequence) -> None:
        self.id = id
        self.name = name
        self.numeric_sequence = numeric_sequence

    def __str__(self) -> str:
        return str(self.id) + "\n" + str(self.name) + "\n" + str(self.numeric_sequence)