from elevenlabs.client import ElevenLabs
from elevenlabs import play, save, stream, Voice, VoiceSettings
from config import ELEVENLABS_API_KEY

def text_to_speech_with_elevenlabs(text, voice_id="default"):
  try:

    #Create ElevenLabs client
    client = ElevenLabs(api_key=ELEVENLABS_API_KEY)

    # Generate speech from text using the specified voice
    audio_stream = client.generate(text=text, voice=voice_id, stream=True)
    
    # Stream the audio
    stream(audio_stream)
  except Exception as e:
    print(f"Error converting text to speech: {e}")
