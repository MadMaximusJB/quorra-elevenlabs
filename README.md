# quorra-elevenlabs

**This project is no longer maintained. For a maintained and cheaper alternative, please visit: https://github.com/MadMaximusJB/quorra**

This project is a custom voice assistant using GPT-4o and ElevenLabs for advanced voice and text interaction. It also features streaming audio from ElevenLabs to help with latency for larger responses.

### Features

- Voice input with keyboard shortcut (F9)
- Text processing using GPT-4o
- Text-to-speech using ElevenLabs
- Stream audio from ElevenLabs for low latency

### Prerequisites

- Python 3.7 or higher
- An OpenAI API key
- An ElevenLabs API key

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/madmaximusjb/quorra.git
    cd quorra
    ```

2. **Create a virtual environment (optional but recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\\Scripts\\activate`
    ```

3. **Install the required packages:**

    **-Manually install mpv (unofficial) through the Microsoft store or from the mpv homepage for Linux.**

    ```bash
    pip install pyaudio
    ```

    ```bash
    pip install -r requirements.txt
    ```

5. **Set up your API keys:**

    Open `config.py` and replace the placeholders with your actual API keys:

    ```python
    OPENAI_API_KEY = 'YOUR_OPENAI_API_KEY'
    ELEVENLABS_API_KEY = 'YOUR_ELEVENLABS_API_KEY'
    DEFAULT_VOICE_ID = 'custom_voice_id'  # Replace with your custom voice ID
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

```
quorra/
│
├── README.md               # Project documentation
├── requirements.txt        # Required Python packages
├── main.py                 # Main script to run the voice assistant
├── config.py               # Configuration file for API keys and settings
├── utils/                  # Utility modules
│   ├── __init__.py         # Init file for utils package
│   ├── audio_input.py      # Module to handle audio input
│   ├── text_processing.py  # Module to process text using GPT-4o
│   ├── text_to_speech.py   # Module to convert text to speech using ElevenLabs
```

### Details of Each Module

#### `main.py`

The main script that runs the voice assistant. It listens for user input when the F9 key is pressed, processes the input using GPT-4o, and responds with generated speech.

#### `config.py`

Contains the configuration settings for the project, including API keys and the default voice ID.

#### `utils/audio_input.py`

Handles capturing and processing audio input. It uses the `speech_recognition` library to convert voice to text and listens only when the F9 key is pressed.

#### `utils/text_processing.py`

Processes the text input using GPT-4o. It combines the initial instructions with relevant past conversations retrieved from memory to generate contextually relevant responses.

#### `utils/text_to_speech.py`

Converts the text response from GPT-4o to speech using ElevenLabs. It supports custom voices by specifying a voice ID.

### Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

### License

This project is licensed under the GPL-3.0 License.

