from textbase import bot, Message
from textbase.models import OpenAI
from typing import List
import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

mydb = mysql.connector.connect(
    host = 'cloud.mindsdb.com',
    user = os.environ.get("USER"),
    password = os.environ.get("PASSWORD"),
    port = '3306'
)

# Load your OpenAI API key
OpenAI.api_key = os.environ.get("API_KEY")


# # Prompt for GPT-3.5 Turbo
# SYSTEM_PROMPT = """
# In less than 300 characters, write a Twitter response in the following format:\
# , <respond like you are a fusion of Kanye West and Albert Einstein. Imagine you possess Kanye's unique style, confidence, and stream-of-consciousness speaking, combined with Einstein's intellect. Use inventive language and metaphors to express ideas with depth. You're known for controversial insights and intellectual brilliance. Make references to Kanye's music and Einstein's scientific achievements.';

# """

cursor = mydb.cursor()

cursor.execute('''SELECT response from mindsdb.yenstein WHERE author_username = "mindsdb" AND text = {{SYSTEM_PROMPT}}''')

for x in cursor:
    SYSTEM_PROMPT = x
    def get_response():
        return SYSTEM_PROMPT
    
@bot()
def on_message(message_history: List[Message], state: dict = None):

    # Generate GPT-3.5 Turbo response
    bot_response = OpenAI.generate(
        system_prompt=SYSTEM_PROMPT,
        message_history=message_history, # Assuming history is the list of user messages
        model="gpt-3.5-turbo",
    )

    response = {
        "data": {
            "messages": [
                {
                    "data_type": "STRING",
                    "value": bot_response
                }
            ],
            "state": state
        },
        "errors": [
            {
                "message": ""
            }
        ]
    }

    return {
        "status_code": 200,
        "response": response
    }