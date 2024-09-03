from PIL import ImageGrab,Image
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key = os.getenv("GEMINI_API_KEY"))

# Cinfiguration
generation_config = {
    'temperature': 0.7,
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

# Taking screenshot and saving it
def take_screenshot():
    path = 'screenshot.jpg'
    
    screenshot = ImageGrab.grab()
    
    rgb_screenshot = screenshot.convert('RGB')
    rgb_screenshot.save(path,quality = 20)
    return path

# Giving the screenshot to the Gemini ai for analysing
def screenshot_vision(prompt):
    photo_path = take_screenshot()
    img = Image.open(photo_path)
    
    prompt = (
        "you are the vision analyst AI that provides semantic meaning from images to provide context"
        "to send to another AI that will create a response to the user.Do not respond as the AI assistant to yhe user."
        "Instead take user prompt input and try to extract all meaning from the photo relevant to the user prompt."
        f"Then generate as much objective data about the image for the AI assistant who will respond to the user. \n USER PROMPT: {prompt}"
    )
    
    response = model.generate_content([prompt,img])
    return response.text