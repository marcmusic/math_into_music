class MusicalSequence:
    def __init__(self, sequence, algorithm_id) -> None:
        self.sequence = sequence
        self.algorithm_id = algorithm_id

    def __str__(self) -> str:
        return str(self.sequence) + "\n" + str(self.algorithm_id)