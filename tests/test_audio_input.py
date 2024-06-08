import unittest
from utils.audio_input import get_audio_input

class TestAudioInput(unittest.TestCase):
    def test_get_audio_input(self):
        # This is a placeholder test; in reality, testing audio input and keybinds requires more complex handling.
        self.assertIsInstance(get_audio_input(), str)

if __name__ == "__main__":
    unittest.main()
