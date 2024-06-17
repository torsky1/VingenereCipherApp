import unittest
from vigenere_cipher.encryption import vigenere_encrypt


class TestEncryption(unittest.TestCase):
    def test_vigenere_encrypt(self):
        self.assertEqual(vigenere_encrypt("HELLO", "KEY"), "RIJVS")


if __name__ == '__main__':
    unittest.main()
