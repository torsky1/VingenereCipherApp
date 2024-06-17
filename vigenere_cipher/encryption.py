def generate_vigenere_table():
    """Function that generate vigenere cipher table"""
    table = []
    for i in range(26):
        row = [(chr((i + j) % 26 + 65)) for j in range(26)]
        table.append(row)
    return table


def vigenere_encrypt(plaintext, key):
    table = generate_vigenere_table()
    key = key.upper()
    plaintext = plaintext.upper()
    encrypted_text = ""

    key_length = len(key)
    key_as_int = [ord(i) - 65 for i in key]  # Convert key characters to numbers (A=0, B=1, ..., Z=25)

    plaintext_index = 0  # Index to keep track of plaintext characters

    for char in plaintext:
        if char.isalpha():
            # Find the index of the key character corresponding to the current plaintext character
            key_index = key_as_int[plaintext_index % key_length]

            # Find the index of the plaintext character in the Vigenere table
            plaintext_index += 1  # Increment index
            plaintext_index %= key_length  # Reset index when it reaches the key length

            # Find the encrypted character using the Vigenere table
            encrypted_index = (ord(char) - 65 + key_index) % 26
            encrypted_char = chr(encrypted_index + 65)

            encrypted_text += encrypted_char
        else:
            # If the character is not alphabetic, keep it unchanged (including spaces)
            encrypted_text += char

    return encrypted_text

