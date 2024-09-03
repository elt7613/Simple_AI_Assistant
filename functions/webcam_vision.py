from PIL import Image
import cv2
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key = os.getenv("GEMINI_API_KEY"))

# Configurations
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

# For accessing the webcam and taking the picture and saving it
def web_cam_capture():
    web_cam = cv2.VideoCapture(0)
    if not web_cam.isOpened():
        print("Error: Camera did not open")
        exit()
        
    path = 'webcam.jpg'
    
    ret,frame = web_cam.read()
    cv2.imwrite(path,frame)
    return path

# Giving the image to the Gemini ai for analysing
def webcam_vision(prompt):
    photo_path = web_cam_capture()
    img = Image.open(photo_path)
    
    prompt = (
        "you are the vision analyst AI that provides semantic meaning from images to provide context"
        "to send to another AI that will create a response to the user.Do not respond as the AI assistant to yhe user."
        "Instead take user prompt input and try to extract all meaning from the photo relevant to the user prompt."
        f"Then generate as much objective data about the image for the AI assistant who will respond to the user. \n USER PROMPT: {prompt}"
    )
    
    response = model.generate_content([prompt,img])
    return response.text