import chainlit as cl
from chatbot import AIbot
from Agent import AIagent
import asyncio
@cl.on_chat_start
async def on_chat_start():
    await cl.Message(content="I am your Ai Assistant!").send()

@cl.on_message
async def main(message: cl.Message):
    user_input = message.content

    # response = AIbot(user_input)
    response = asyncio.run(AIagent(user_input))


    await cl.Message(content=f"{response}").send()