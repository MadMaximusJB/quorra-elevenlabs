import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

# Define the initial instructions for the assistant
INITIAL_PROMPT = (
    "You are an intelligent voice assistant. You will respond to user queries "
    "in a friendly and helpful manner. Always be concise and provide useful information. Your name is Quorra."
)

def process_text_with_gpt4o(text):
    try:
        # Combine the initial instructions with the user input
        prompt = INITIAL_PROMPT + "\n\nUser: " + text + "\nAssistant:"
        
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150
        )
        
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"Error processing text with GPT-4o: {e}")
        return None
