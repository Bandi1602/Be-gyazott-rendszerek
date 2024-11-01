from random import randint

ALPHABET = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ"


def generate_otp(characters):
    with open("otp.txt", "w") as f:
        for i in range(characters):
            f.write(str(randint(0, 26)) + "\n")


def load_otp():
    with open("otp.txt", "r") as f:
        contents = f.read().splitlines()
    return contents


#                   decrypt: -key
def encrypt(message, key):
    ciphertext = ""
    for position, character in enumerate(message):
        if character not in ALPHABET:
            ciphertext += character
        else:
            encrypted = (ALPHABET.index(character) + int(key[position])) % len(ALPHABET)
            ciphertext += ALPHABET[encrypted]
    return ciphertext


def decrypt(encrypted_message, key):
    decrypted_message = ""
    for position, character in enumerate(encrypted_message):
        if character not in ALPHABET:
            decrypted_message += character
        else:
            decrypted = (ALPHABET.index(character) - int(key[position])) % len(ALPHABET)
            decrypted_message += ALPHABET[decrypted]
    return decrypted_message


def main():
    otp_length = 100
    generate_otp(otp_length)

    otp = load_otp()

    message = input("Enter the message you want to encrypt: ").lower()

    encrypted_message = encrypt(message, otp)
    print("Encrypted message:", encrypted_message)

    decrypted_message = decrypt(encrypted_message, otp)
    print("Encrypted message:", decrypted_message)


##############################################################################

if __name__ == "__main__":
    main()
