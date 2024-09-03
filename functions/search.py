from duckduckgo_search import DDGS
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

groq_client = Groq(api_key=os.getenv("GROQ_API_KEY2"))

system_message = ("""
        You are an AI Online information searcher using the search tool.
        You will respond the best searching sentence according to the user's prompt with the topic for the google search.

        Analyse the user's prompt and the previous conversation,find out what the user is saying and about what topic and about whom he is looking for to search, respond only the sentence mentioning about whom or who or what that could be used to get the perfect result in google search.
        Do not respond any explanation or indicating that the task is done or with quotes,just respond the sentence that could be used to search the relavent information from the google search.
    """)

messages = []
messages.append({"role": "system","content": system_message})
def Online_search(prompt: str) -> str:
    messages.append({"role": "user","content": prompt})

    chat_completion = groq_client.chat.completions.create(
        temperature = 0,
        model = "llama3-70b-8192",
        messages = messages
    )
     
    response = chat_completion.choices[0].message.content
    messages.append({"role": "assistant","content": response})
    # print(f"Need to Search: {response}")
    
    results = DDGS().text(str(response), max_results=5)
    # print(f"Searched result: {results}")
    
    return results