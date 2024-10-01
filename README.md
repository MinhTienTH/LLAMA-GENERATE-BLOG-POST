# Generative Blog Post Creator

This project is a Streamlit web application that uses the Hugging Face Hub to generate blog posts based on user input.

## Features

- Generate blog posts with customizable parameters:
  - Number of words
  - Blog post title
  - Writing style

## Requirements

- Python 3.7+
- Streamlit
- LangChain
- Hugging Face Hub

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/MinhTienTH/blogpost.git
   cd generative-blog-post-creator
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Set up your Hugging Face Hub API token:
   - Sign up for a Hugging Face account and get your API token
   - Replace the empty string in `main.py` with your token:
     ```python
     HUGGINGFACEHUB_API_TOKEN = "your_token_here"
     ```

## Usage

1. Run the Streamlit app:
   ```
   streamlit run main.py
   ```

2. Open your web browser and go to the URL provided by Streamlit (usually `http://localhost:8501`)

3. Use the interface to set your desired parameters and generate a blog post

## How it Works

The application uses the LangChain library to create a prompt template and interact with the Hugging Face Hub's language model (Llama-2-7b-chat-hf). The user's input is formatted into a prompt, which is then sent to the language model to generate the blog post content.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).
