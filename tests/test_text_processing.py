import unittest
from utils.text_processing import process_text_with_gpt4o

class TestTextProcessing(unittest.TestCase):
    def test_process_text_with_gpt4o(self):
        response = process_text_with_gpt4o("Hello, how are you?")
        self.assertIsInstance(response, str)

if __name__ == "__main__":
    unittest.main()
