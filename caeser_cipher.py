from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
program_run = True
print(logo)

def encode(txt, sift_number):
    encoded_text = ''
    for letter in txt:
        if letter == ' ':
            encoded_text += ' '
        else:
            new_index = alphabet.index(f'{letter}') + sift_number
            if new_index > len(alphabet):
                new_index = new_index - 27
            encoded_text += alphabet[new_index]

    print(f"Your encoded text is :{encoded_text}")


def decode(txt, sift_number):
    decoded_text = ''
    for letter in txt:
        new_index = alphabet.index(f'{letter}') - sift_number
        if new_index < 0:
            new_index = new_index + 27
        decoded_text += alphabet[new_index]

    print(f"Your decoded text is :{decoded_text}")


while program_run:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if direction == "encode":
        encode(text, shift)
    elif direction == "decode":
        decode(text, shift)
    else:
        print(f"Your command {direction} do not exist!")

    restart = input(f"Do you want to restart program? Type 'y' or 'n'?").lower()
    if restart == 'n':
        program_run = False