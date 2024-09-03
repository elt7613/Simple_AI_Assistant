from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

groq_client = Groq(api_key=os.getenv("GROQ_API_KEY3"))

# System message 
system_message = ("""
        You are an AI function-calling model.
        Check if user's prompt is an automation or a query.
        You will determine the best action for a voice assistant to respond to the user's prompt from the following list: 
        ['extract clipboard', 'take screenshot', 'capture webcam', 'search online','None'].

        If the user mentions "search" or "google search" or asks for the news, respond with 'search online'.
        If the user ask what's on my screen or what do you see on my scren,respond with 'take screenshot'.
        If the user ask acces my webcam/camera or what you see from my webcam/camera or what am i holding or what is on my hand or what do you see,respond with 'capture webcam'.
        If the user asks to explain from the clipboard that he has just copied or asks i have compied something explain,respond with 'extract clipboard'.
        IF the user asks to search the news or search someting online to get real time data,respond 'search online'.
        Assume the webcam is a normal laptop webcam facing the user.
        
        Respond with only one selection from the list and do not provide any explanations. 
        Format the function call name exactly as listed.
    """)

# Function to response the function to be used
function_messages = [{"role": "system", "content": system_message}]
def function_call(prompt):
    function_messages.append({"role": "user", "content": prompt})
    
    chat_completion = groq_client.chat.completions.create(
        model = "llama3-70b-8192",
        messages = function_messages,
    )
     
    response = chat_completion.choices[0].message.content 
    function_messages.append({"role": "assistant", "content": response})
    return response