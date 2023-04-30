class DiatonicMode:
    def __init__(self, name, offset) -> None:
        self.name = name
        self.offset = offset

    def __str__(self) -> str:
        return str(self.name) + "\n" + str(self.offset)