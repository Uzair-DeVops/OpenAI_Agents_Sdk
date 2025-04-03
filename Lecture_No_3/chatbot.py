from litellm import completion
import os
from dotenv import load_dotenv

load_dotenv()
## set ENV variables

def AIbot(user_query):
    response = completion(
    model="gemini/gemini-2.0-flash-exp",
    messages=[{ "content": user_query,"role": "user"}]
    )

    return (response["choices"][0]["message"]["content"])


print(AIbot("hello"))