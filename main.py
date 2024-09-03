from llm import Assistant
from function_calling import function_call
from functions.clipboard import clipboard
from functions.screenshot_vision import screenshot_vision
from functions.webcam_vision import webcam_vision
from functions.search import Online_search
from functions.speak import Speak
from functions.listen import Listen

while True:
    # prompt = input("\nUser: ")
    prompt = Listen()
    print(f"\nYOU:  {prompt} \n")
    
    try:
        call = function_call(prompt) # Checks which function to use
        print(f"Function Call: {call}")

        if "take screenshot" in call:
            print("Taking screenshot")
            screenshot_context = screenshot_vision(prompt)
            webcam_context = None
            clipboard_context = None
            online_search = None 
        elif "capture webcam" in call:
            print("Capturing webcam")
            webcam_context = webcam_vision(prompt)
            screenshot_context = None
            clipboard_context = None
            online_search = None 
        elif "extract clipboard" in call:
            clipboard_context = clipboard(prompt)
            webcam_context = None
            screenshot_context = None
            online_search = None 
        elif "search online" in call:
            online_search = Online_search(prompt)
            clipboard_context = None
            webcam_context = None
            screenshot_context = None
        else:
            clipboard_context = None
            webcam_context = None
            screenshot_context = None  
            online_search = None  
            
        response = Assistant(f"{prompt}",webcam_context,screenshot_context,online_search,clipboard_context)
        print(f"\n>> Assistant: {response} \n")
        Speak(response)
        
    except Exception as e:
        print(f"ERROR: {e}")       

    
    
    

