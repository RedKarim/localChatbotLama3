import gradio as gr
import requests
import json
import PyPDF2
import os

def read_pdf(pdf_path):
    """Extract text from PDF file"""
    text = ""
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            for page in pdf_reader.pages:
                text += page.extract_text()
        return text
    except Exception as e:
        return f"Error reading PDF: {str(e)}"

def generate_response(message, history):
    # Load CV text
    cv_text = read_pdf("cv.pdf")
    
    # Ollama API endpoint
    url = "http://localhost:11434/api/generate"
    
    # Create a system prompt that includes the CV context
    system_prompt = f"""You are a helpful AI assistant that has access to the following CV/resume:

{cv_text}

Please answer questions about this CV accurately based on the information provided above. 
If a question cannot be answered based on the information in the CV, please say so.
"""
    
    # Prepare the conversation history
    conversation = f"System: {system_prompt}\n"
    for user_msg, assistant_msg in history:
        conversation += f"User: {user_msg}\nAssistant: {assistant_msg}\n"
    conversation += f"User: {message}\nAssistant:"
    
    # Prepare the request payload
    payload = {
        "model": "llama3.2",
        "prompt": conversation,
        "stream": False,
        "temperature": 0.7,
        "max_tokens": 2000
    }
    
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        result = response.json()
        return result["response"]
    except requests.exceptions.RequestException as e:
        return f"Error: {str(e)}\nMake sure Ollama is running with llama2:3.2 model loaded."

# Verify CV file exists
cv_path = "cv.pdf"
if not os.path.exists(cv_path):
    print(f"Error: {cv_path} not found in the current directory!")
    print(f"Current directory: {os.getcwd()}")
    exit(1)

# Create the Gradio interface
demo = gr.ChatInterface(
    fn=generate_response,
    title="CV Question Answering System",
    description="Ask questions about your CV. The system has already loaded your CV.pdf file.",
    examples=[
        "What is my work experience?",
        "What are my key skills?",
        "What is my educational background?",
        "What programming languages do I know?",
        "Summarize my CV",
        "What are my main achievements?"
    ]
)

# Launch the interface
if __name__ == "__main__":
    print("CV loaded successfully! Starting chat interface...")
    demo.launch(share=False, inbrowser=True)