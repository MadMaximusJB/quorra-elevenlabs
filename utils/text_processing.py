from openai import OpenAI
from config import OPENAI_API_KEY

def process_text_with_gpt4o(text):
    try:
        ## Set the API key
        client = OpenAI(api_key=OPENAI_API_KEY)
        
        # Combine the initial instructions with the user input
        prompt = text 
        
        MODEL="gpt-4o"

        completion = client.chat.completions.create(
        model=MODEL,
        messages=[
        {"role": "system", "content": "You are an intelligent voice assistant. You will respond to user queries "
        "in a friendly and helpful manner. Always be concise and provide useful information. Your name is Quorra, you are a young to middle aged female."},
        {"role": "user", "content": prompt}
        ]
        )
        return completion.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error processing text with GPT-4o: {e}")
        return None
