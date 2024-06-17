def generate_vigenere_table():
    """Function that generate vigenere cipher table"""
    table = []
    for i in range(26):
        row = [(chr((i + j) % 26 + 65)) for j in range(26)]
        table.append(row)
    return table


def vigenere_decrypt(ciphertext, key):
    table = generate_vigenere_table()
    key = key.upper()
    ciphertext = ciphertext.upper()
    decrypted_text = ""

    key_length = len(key)
    key_as_int = [ord(i) - 65 for i in key]  # Convert key characters to numbers (A=0, B=1, ..., Z=25)
    ciphertext_index = 0  # Index to keep track of ciphertext characters

    for char in ciphertext:
        if char.isalpha():
            # Find the index of the key character corresponding to the current ciphertext character
            key_index = key_as_int[ciphertext_index % key_length]

            # Find the index of the decrypted character using the Vigenere table
            decrypted_index = (ord(char) - 65 - key_index) % 26
            decrypted_char = chr(decrypted_index + 65)

            decrypted_text += decrypted_char

            # Increment the index for the next ciphertext character
            ciphertext_index += 1
        else:
            # If the character is not alphabetic, keep it unchanged (including spaces)
            decrypted_text += char

    return decrypted_text
