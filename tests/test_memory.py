import unittest
from utils.memory import Memory

class TestMemory(unittest.TestCase):
    def setUp(self):
        self.memory = Memory()

    def test_add_to_memory(self):
        text = "Hello, how are you?"
        response = "I am fine, thank you."
        index_size = self.memory.add_to_memory(text, response)
        self.assertEqual(index_size, 1)

    def test_search_memory(self):
        text = "Hello, how are you?"
        response = "I am fine, thank you."
        self.memory.add_to_memory(text, response)
        results = self.memory.search_memory("How are you?")
        self.assertEqual(len(results), 1)

    def test_retrieve_metadata(self):
        text = "Hello, how are you?"
        response = "I am fine, thank you."
        self.memory.add_to_memory(text, response)
        results = self.memory.search_memory("How are you?")
        metadata = self.memory.retrieve_metadata(results)
        self.assertEqual(len(metadata), 1)
        self.assertIn('timestamp', metadata[0])
        self.assertEqual(metadata[0]['text'], text)
        self.assertEqual(metadata[0]['response'], response)

if __name__ == "__main__":
    unittest.main()
