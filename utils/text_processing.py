import openai
from config import OPENAI_API_KEY
from utils.memory import memory

openai.api_key = OPENAI_API_KEY

# Define the initial instructions for the assistant
INITIAL_PROMPT = (
    "You are an intelligent voice assistant. You will respond to user queries "
    "in a friendly and helpful manner. Always be concise and provide useful information. Your name is Quorra."
)

def process_text_with_gpt4o(text):
    try:
        # Search memory for relevant past conversations
        memory_ids = memory.search_memory(text)
        memory_items = memory.retrieve_metadata(memory_ids)
        
        # Format memory items to include in the prompt
        memory_context = "\n".join(
            [f"[{item['timestamp']}] User: {item['text']} - Assistant: {item['response']}" for item in memory_items]
        )

        # Combine the initial instructions with the memory and user input
        prompt = INITIAL_PROMPT + "\n\n" + memory_context + "\n\nUser: " + text + "\nAssistant:"
        
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150
        )

        # Add the conversation to memory
        memory.add_to_memory(text, response.choices[0].text.strip())
        
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"Error processing text with GPT-4o: {e}")
        return None
