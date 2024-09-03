from elevenlabs import play
from elevenlabs.client import ElevenLabs
import os
from dotenv import load_dotenv

load_dotenv()

client = ElevenLabs(
  api_key = os.getenv("ELEVENLABS_API_KEY")
)

def Speak(text):
    audio = client.generate(
      text = text,
      voice = "Andrew Tate",
      model = "eleven_multilingual_v2"
    )
    play(audio)
    

