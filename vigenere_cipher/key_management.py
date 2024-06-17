from tkinter import filedialog
import secrets
import string


def generate_secure_key(length=16):
    alphabet = string.ascii_uppercase  # Limiting to uppercase letters for Vigenere cipher
    key = ''.join(secrets.choice(alphabet) for _ in range(length))
    return key


def save_key_to_file(key):
    filepath = (
        filedialog.asksaveasfilename(defaultextension=".key", filetypes=[("Key files", "*.key"), ("All files", "*.*")]))
    if filepath:
        with open(filepath, 'w') as file:
            file.write(key)
        return filepath
    return None


def load_key_from_file():
    filepath = filedialog.askopenfilename(filetypes=[("Key files", "*.key"), ("All files", "*.*")])
    if filepath:
        with open(filepath, 'r') as file:
            key = file.read().strip()
        return key
    return None


def save_message_to_file(encrypted_text):
    filepath = (
        filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("txt files", "*.txt"), ("All files", "*.*")]))
    if filepath:
        with open(filepath, 'w') as file:
            file.write(encrypted_text)
        return filepath
    return None


def load_message_from_file():
    filepath = filedialog.askopenfilename(filetypes=[("Key files", "*.txt"), ("All files", "*.*")])
    if filepath:
        with open(filepath, 'r') as file:
            encrypted_text = file.read().strip()
        return encrypted_text
    return None
