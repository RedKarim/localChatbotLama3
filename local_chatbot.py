import gradio as gr
import requests
import json

def generate_response(message, history):
    # Ollama API endpoint (default local URL)
    url = "http://localhost:11434/api/generate"
    
    # Prepare the prompt with conversation history
    conversation = ""
    for user_msg, assistant_msg in history:
        conversation += f"User: {user_msg}\nAssistant: {assistant_msg}\n"
    conversation += f"User: {message}\nAssistant:"
    
    # Prepare the request payload
    payload = {
        "model": "llama3.2",  # Updated to use Llama2 3.2
        "prompt": conversation,
        "stream": False,
        "temperature": 0.7,  # Added temperature for better response variety
        "max_tokens": 2000    # Added max tokens to control response length
    }
    
    try:
        # Make the API request
        response = requests.post(url, json=payload)
        response.raise_for_status()  # Raise an exception for bad status codes
        
        # Extract the response text
        result = response.json()
        return result["response"]
        
    except requests.exceptions.RequestException as e:
        return f"Error: {str(e)}\nMake sure Ollama is running with llama2:3.2 model loaded."

# Create the Gradio interface
demo = gr.ChatInterface(
    fn=generate_response,
    title="Local LLM Chat (Llama2 3.2)",
    description="Chat with locally hosted Llama2 3.2 model via Ollama",
    examples=["Hello, how are you?", 
             "Explain quantum computing in simple terms", 
             "Write a creative story about space exploration"]
)

# Launch the interface
if __name__ == "__main__":
    demo.launch(share=False, inbrowser=True)