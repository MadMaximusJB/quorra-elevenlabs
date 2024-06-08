# quorra

This project is a custom voice assistant using GPT-4o and ElevenLabs for advanced voice and text interaction. It features long-term memory by vectorizing conversations and recalling relevant past interactions.

### Features

- Voice input with keyboard shortcut (F9)
- Text processing using GPT-4o
- Text-to-speech using ElevenLabs
- Long-term memory with timestamped conversations
- Recall of relevant past interactions using vector embeddings

### Prerequisites

- Python 3.7 or higher
- An OpenAI API key
- An ElevenLabs API key

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/voice_assistant.git
    cd voice_assistant
    ```

2. **Create a virtual environment (optional but recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\\Scripts\\activate`
    ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up your API keys:**

    Open `config.py` and replace the placeholders with your actual API keys:

    ```python
    OPENAI_API_KEY = 'YOUR_OPENAI_API_KEY'
    ELEVENLABS_API_KEY = 'YOUR_ELEVENLABS_API_KEY'
    DEFAULT_VOICE_ID = 'custom_voice_id'  # Replace with your custom voice ID
    EMBEDDING_ENGINE = 'text-embedding-ada-002'  # Replace with the actual engine if needed
    ```

### Usage

1. **Run the voice assistant:**

    ```bash
    python main.py
    ```

2. **Interact with the assistant:**

    - Press and hold `F9` to start listening.
    - Speak your query clearly into the microphone.
    - Release `F9` to process your input and get a response.

### Project Structure


