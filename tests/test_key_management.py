import unittest
from unittest.mock import patch
from vigenere_cipher.key_management import save_key_to_file, load_key_from_file


class TestKeyManagement(unittest.TestCase):
    @patch('vigenere_cipher.key_management.filedialog.asksaveasfilename', return_value="test.key")
    @patch('builtins.open', new_callable=unittest.mock.mock_open)
    def test_save_key_to_file(self, mock_open, mock_dialog):
        save_key_to_file("TEST_KEY")
        mock_open.assert_called_with("test.key", 'w')

    @patch('vigenere_cipher.key_management.filedialog.askopenfilename', return_value="test.key")
    @patch('builtins.open', new_callable=unittest.mock.mock_open, read_data="TEST_KEY")
    def test_load_key_from_file(self, mock_open, mock_dialog):
        key = load_key_from_file()
        self.assertEqual(key, "TEST_KEY")


if __name__ == '__main__':
    unittest.main()
