import unittest
from vigenere_cipher.decryption import vigenere_decrypt


class TestDecryption(unittest.TestCase):
    def test_vigenere_decrypt(self):
        self.assertEqual(vigenere_decrypt("RIJVS", "KEY"), "HELLO")


if __name__ == '__main__':
    unittest.main()
