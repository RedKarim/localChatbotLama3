# Local CV Chatbot with Llama 2

A local chatbot that uses Llama 2 (via Ollama) to answer questions about your CV/resume. This application provides an intuitive chat interface where you can ask questions about your CV and get AI-powered responses.

## Features

- 🤖 Powered by Llama 2 (3.2) running locally through Ollama
- 💬 Interactive chat interface built with Gradio
- 📄 Automatic PDF parsing of your CV
- 🔒 Completely local - your CV data never leaves your computer
- ❓ Example questions provided for easy starting points

## Prerequisites

- Python 3.8+
- Ollama installed with Llama 2 (3.2) model
- Your CV in PDF format

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/local-cv-chatbot.git
cd local-cv-chatbot
```

2. Install required Python packages:
```bash
pip install gradio requests PyPDF2
```

3. Install Ollama and download Llama 2 (if not already done):
```bash
ollama pull llama2:3.2
```

## Usage

1. Place your CV (named `cv.pdf`) in the same directory as the script

2. Start Llama 2 in Ollama:
```bash
ollama run llama2:3.2
```

3. Run the chatbot:
```bash
python cv_chatbot.py
```

4. Open your web browser and navigate to `http://localhost:7860` (opens automatically)

5. Start asking questions about your CV!

## Example Questions

- "What is my work experience?"
- "What are my key skills?"
- "What is my educational background?"
- "What programming languages do I know?"
- "Summarize my CV"
- "What are my main achievements?"

## How It Works

1. The application reads your CV using PyPDF2
2. When you ask a question, it sends the CV content and your question to the local Llama 2 model
3. The model processes your question in the context of your CV
4. Responses are displayed in a chat-like interface

## Technical Details

- **Backend**: Python with Ollama API
- **Frontend**: Gradio web interface
- **Model**: Llama 2 (3.2)
- **PDF Processing**: PyPDF2

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License - feel free to use this project however you'd like!

## Privacy Note

All processing is done locally on your machine. Your CV and questions never leave your computer, making this a privacy-friendly solution for CV analysis.

## Future Improvements

- [ ] Support for more document formats (DOCX, TXT)
- [ ] Advanced CV parsing with section recognition
- [ ] Job description matching
- [ ] Automatic CV summarization
- [ ] Custom prompt templates
- [ ] Export conversation history

## Troubleshooting

If you encounter any issues:

1. Ensure Ollama is running with Llama 2 model
2. Check that your CV is properly named and placed
3. Verify all dependencies are installed
4. Check console output for error messages

## Support

If you find this project helpful, please star it on GitHub! For issues or questions, please open an issue in the repository.
