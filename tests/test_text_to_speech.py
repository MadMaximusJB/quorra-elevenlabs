import unittest
from utils.text_to_speech import text_to_speech_with_elevenlabs

class TestTextToSpeech(unittest.TestCase):
    def test_text_to_speech_with_elevenlabs(self):
        # This is a placeholder test; testing text-to-speech requires more complex handling.
        self.assertIsNone(text_to_speech_with_elevenlabs("Hello, this is a test."))

if __name__ == "__main__":
    unittest.main()
