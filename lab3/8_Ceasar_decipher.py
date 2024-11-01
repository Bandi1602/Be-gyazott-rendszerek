def caesar_decrypt(encrypted_message):
    decrypted_messages = []

    # Loop through all possible keys (0 to 25) to decrypt the message
    for key in range(26):
        decrypted_message = ""

        # Decrypt the message using the current key
        for char in encrypted_message:
            if char.isalpha():
                shifted = ord(char) - key
                if char.islower():
                    if shifted < ord("a"):
                        shifted += 26
                elif char.isupper():
                    if shifted < ord("A"):
                        shifted += 26
                decrypted_message += chr(shifted)
            else:
                decrypted_message += char

        decrypted_messages.append((key, decrypted_message))

    return decrypted_messages


# Example usage
encrypted_message = "iqfihhih"
results = caesar_decrypt(encrypted_message)

for key, message in results:
    print(f"Key {key}: {message}")
