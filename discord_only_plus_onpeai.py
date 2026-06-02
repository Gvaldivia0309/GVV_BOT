from dotenv import load_dotenv
from openai import OpenAI # OpenAI library
import discord
import os

#set openai api key
load_dotenv()
OPENAI_KEY = os.getenv('OPENAI_KEY')
oa_client = OpenAI(api_key=OPENAI_KEY)

#ask openai - respond like a AeroSpace
def call_openai(question):
  
