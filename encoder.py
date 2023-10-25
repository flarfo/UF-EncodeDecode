class Encoder:
    def __init__(self) -> None:
        self.password =""

    # Where password is an 8-digit string
    def encode(self, password: str):
        self.password = ''.join([str(int(digit) + 3) for digit in password])
        return self.password
    def decode(self, password):
        decoded = ""
        for x in password:
            x = int(x) - 3
            decoded = decoded + str(x)
        return decoded
    
def main():
    encoder = Encoder()
    password = 0
    decoded = 0

    while True:
        choice = input('Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n\nPlease enter an option: ')

        match choice:
            case '1':
                password = encoder.encode(input('Please enter your password to encode: '))
                print('Your password has been encoded and stored!\n')
            case '2':
                decoded = encoder.decode(password)
                print(f"The encoded password is {password}, and the original password is {decoded}.")
                pass
            case '3':
                quit()

if __name__ == '__main__':
    main()