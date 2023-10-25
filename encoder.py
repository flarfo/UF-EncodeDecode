class Encoder:
    def __init__(self, password) -> None:
        self.password = self.encode(password)

    # Where password is an 8-digit string
    def encode(self, password: str):
        return ''.join([str(int(digit) + 3) for digit in password])