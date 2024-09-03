from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

groq_client = Groq(api_key=os.getenv("GROQ_API_KEY1"))

system_message = (
    "You are an AI voice assistant.Your user may or may not have attached a photo for content(either a screenshot or a webcam capture)."
    "Any photo has already been processed into a highly detailed text prompt that will be attacthed to their transcribed voice prompt.Generate the most useful and "
    "factual response possible,carefully considering all previous generated text in your response before adding new tokens to the response."
    "Do not expect or request images,just use the context if added."
    "Use all of the context of this converstion so your response is relevant to the converstion."
    "Make your response clear and concise,avoiding any verbosity."
    
    " ***Give a short response just like Jarvis***"
)

messages = [{'role': 'system','content': system_message}]

def Assistant(prompt,webcam_context,screenshot_context,online_search,clipboard_context):
    if webcam_context:
        prompt = f"USER PROMPT: {prompt}\n\n WEBCAM CONTEXT: {webcam_context}"
        
    if screenshot_context:
        prompt = f"USER PROMPT: {prompt}\n\n SCREENSHOT CONTEXT: {screenshot_context}"
    
    if online_search:
        prompt = f"USER PROMPT: {prompt}\n\n ONLINE SEARCH CONTEXT: {online_search}"
        
    if clipboard_context:
        prompt = f"USER PROMPT: {prompt}\n\n CLIPBOARD CONTEXT: {clipboard_context}"
    
    messages.append({'role': 'user','content': prompt})
    
    chat_completion = groq_client.chat.completions.create(
        temperature = 0.7,
        model = "llama-3.1-70b-versatile",
        messages = messages
    )
    
    response = chat_completion.choices[0].message.content
    messages.append({'role': 'assistant','content': response})
    
    return response

