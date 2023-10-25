class Encoder:
    def __init__(self) -> None:
        pass

    # Where password is an 8-digit string
    def encode(self, password: str):
        return ''.join([str(int(digit) + 3) for digit in password])
    
def main():
    encoder = Encoder()

    while True:
        choice = input('Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n\nPlease enter an option: ')

        match choice:
            case '1':
                encoder.encode(input('Please enter your password to encode: '))
                print('Your password has been encoded and stored!\n')
            case '2':
                # Decode here
                pass
            case '3':
                quit()

if __name__ == '__main__':
    main()