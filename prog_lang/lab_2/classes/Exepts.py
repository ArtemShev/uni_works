class IncorrectArgExeption(Exception):
    def __init__(self, arg):
        self.arg = arg

    def __str__(self) -> str:
        return f"{self.arg} - incorrect id"


class NonExistentExeption(Exception):
    def __init__(self, arg):
        self.arg = arg

    def __str__(self) -> str:

        return f"{self.arg} - non-existent"