import tkinter as tk
from tkinter import ttk, messagebox
from vigenere_cipher.encryption import vigenere_encrypt
from vigenere_cipher.decryption import vigenere_decrypt
from vigenere_cipher.key_management import (save_key_to_file, load_key_from_file, save_message_to_file,
                                            load_message_from_file, generate_secure_key)


def encrypt_text():
    """Function that encrypt out message"""
    plaintext = plaintext_entry.get()
    key = key_entry.get()
    if not plaintext or not key:
        messagebox.showerror("Error", "Please enter both plaintext and key")
        return

    encrypted_text = vigenere_encrypt(plaintext, key)
    result_text.set(encrypted_text)


def decrypt_text():
    """Function that dencrypt out message"""
    ciphertext = plaintext_entry.get()
    key = key_entry.get()
    if not ciphertext or not key:
        messagebox.showerror("Error", "Please enter both ciphertext and key")
        return

    decrypted_text = vigenere_decrypt(ciphertext, key)
    result_text.set(decrypted_text)


def save_key():
    """Function that saves our key"""
    key = key_entry.get()
    if not key:
        messagebox.showerror("Error", "Please enter a key to save")
        return
    save_key_to_file(key)


def load_key():
    """Function that loads our key"""
    key = load_key_from_file()
    if key:
        key_entry.delete(0, tk.END)
        key_entry.insert(0, key)


def save_message():
    """Function that saves our response"""
    encrypted_text = result_text.get()
    if not result_text:
        messagebox.showerror("Error", "Result is incorrect")
        return
    save_message_to_file(encrypted_text)


def load_message():
    """Function that loads our saved response"""
    encrypted_text = load_message_from_file()
    if encrypted_text:
        plaintext_entry.delete(0, tk.END)
        plaintext_entry.insert(0, encrypted_text)


def generate_key():
    """Function generating random safe key"""
    key = generate_secure_key()
    key_entry.delete(0, tk.END)
    key_entry.insert(0, key)


def clear_fields():
    """Function to clear all fields"""
    plaintext_entry.delete(0, tk.END)
    key_entry.delete(0, tk.END)
    result_text.set("")


def run_app():
    """Create the main application window"""
    global plaintext_entry, key_entry, result_text

    root = tk.Tk()
    root.title("Vigenere Cipher Encryption")
    root.configure(bg='grey70')
    root.geometry("600x550")

    style = ttk.Style(root)
    style.theme_use("clam")
    style.configure("TButton", padding=10, relief="flat", background="grey26", foreground="black")
    style.configure("TEntry", padding=5, relief="flat", background="white", foreground="black",
                    fieldbackground="grey70")

    frame = ttk.Frame(root, padding="20 20 20 20", style="TFrame")
    frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0, weight=1)

    plaintext_label = ttk.Label(frame, text="Enter your text", font=("Arial", 14))
    plaintext_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
    plaintext_entry = ttk.Entry(frame, width=50)
    plaintext_entry.grid(row=1, column=0, padx=10, pady=5, sticky=(tk.W, tk.E))

    key_label = ttk.Label(frame, text="Enter your key", font=("Arial", 14))
    key_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)
    key_entry = ttk.Entry(frame, width=50)
    key_entry.grid(row=3, column=0, padx=10, pady=5, sticky=(tk.W, tk.E))

    encrypt_button = ttk.Button(frame, text="Encrypt", command=encrypt_text)
    encrypt_button.grid(row=4, column=0, padx=10, pady=10, sticky=tk.W)

    decrypt_button = ttk.Button(frame, text="Decrypt", command=decrypt_text)
    decrypt_button.grid(row=4, column=1, padx=10, pady=10, sticky=tk.W)

    generate_key_button = ttk.Button(frame, text="Generate Key", command=generate_key)
    generate_key_button.grid(row=5, column=0, padx=10, pady=10, sticky=tk.W)

    save_key_button = ttk.Button(frame, text="Save Key", command=save_key)
    save_key_button.grid(row=5, column=1, padx=10, pady=10, sticky=tk.W)

    load_key_button = ttk.Button(frame, text="Load Key", command=load_key)
    load_key_button.grid(row=6, column=0, padx=10, pady=10, sticky=tk.W)

    save_message_button = ttk.Button(frame, text="Save Encrypted", command=save_message)
    save_message_button.grid(row=6, column=1, padx=10, pady=10, sticky=tk.W)

    load_message_button = ttk.Button(frame, text="Load Encrypted", command=load_message)
    load_message_button.grid(row=7, column=0, padx=10, pady=10, sticky=tk.W)

    clear_button = ttk.Button(frame, text="Clear", command=clear_fields)
    clear_button.grid(row=7, column=1, padx=10, pady=10, sticky=tk.W)

    result_label = ttk.Label(frame, text="Result", font=("Arial", 14))
    result_label.grid(row=8, column=0, padx=10, pady=10, sticky=tk.W)
    result_text = tk.StringVar()
    result_entry = ttk.Entry(frame, textvariable=result_text, width=50)
    result_entry.grid(row=9, column=0, padx=10, pady=5, sticky=(tk.W, tk.E))

    root.mainloop()


if __name__ == "__main__":
    run_app()
