from elevenlabs import generate, play
from config import ELEVENLABS_API_KEY

def text_to_speech_with_elevenlabs(text, voice_id="default"):
    try:
        # Generate speech from text using the specified voice
        audio = generate(text, api_key=ELEVENLABS_API_KEY, voice=voice_id)
        # Play the generated audio
        play(audio)
    except Exception as e:
        print(f"Error converting text to speech: {e}")
