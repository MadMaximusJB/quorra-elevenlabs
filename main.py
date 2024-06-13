from utils.audio_input import get_audio_input
from utils.text_processing import process_text_with_gpt4o
from utils.text_to_speech import text_to_speech_with_elevenlabs
from config import DEFAULT_VOICE_ID
import keyboard

def main(voice_id=DEFAULT_VOICE_ID):
    while True:
        user_input = get_audio_input()
        
        if user_input:
            response_text = process_text_with_gpt4o(user_input)
            
            if response_text:
                print(f"Assistant: {response_text}")
                text_to_speech_with_elevenlabs(response_text, voice_id=voice_id)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Exiting Quorra.")
