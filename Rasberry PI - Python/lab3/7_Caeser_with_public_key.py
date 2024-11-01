def caesar_encryption(msg):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    privare_key = 19
    encry_message = ""

    for c in msg:
        position = alphabet.find(c)
        new_position = (position + privare_key) % len(alphabet)
        new_character = alphabet[new_position]
        encry_message += new_character
    return encry_message


def caesar_decryption(encrypted_msg, private_key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    decrypted_message = ""

    for c in encrypted_msg:
        if c in alphabet:
            position = alphabet.find(c)
            new_position = (position - private_key) % len(alphabet)
            new_character = alphabet[new_position]
            decrypted_message += new_character
        else:
            # If the character is not in the alphabet (e.g., space or punctuation), keep it unchanged.
            decrypted_message += c

    return decrypted_message


def main():
    message = input("Adj meg egy szovegt: ")
    encryp = caesar_encryption(message)
    print("Encrypted: ", encryp)

    decryp = caesar_decryption(
        encryp, 19
    )  # Use the same private_key (23) for decryption
    print("Decrypted:", decryp)


if __name__ == "__main__":
    main()
