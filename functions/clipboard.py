import pyperclip
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key = os.getenv("GEMINI_API_KEY"))

# Configurations
generation_config = {
    'temperature': 0.5,
    'top_p': 1,
    'top_k': 1,
    'max_output_tokens': 2048
}

# Gemini's safety configuration
safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_NONE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_NONE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_NONE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_NONE"
    },
]

# Defining the model
model = genai.GenerativeModel(
    "gemini-1.5-flash",
    generation_config = generation_config,
    safety_settings = safety_settings
)

# To get the copied clipboard 
def get_clipboard_text():
    clipboard_content = pyperclip.paste()
    if isinstance(clipboard_content,str):
        return clipboard_content
    else:
        print("No clipboard text to copy")
        return None

# Giving the copied clipbord data to the Gemini ai  
def clipboard(userprompt):
    clipboard = get_clipboard_text()
    
    prompt = f"PROMPT: {userprompt} \n\n CLIPBOARD: {clipboard}"
    
    response = model.generate_content(prompt)
    return response.text