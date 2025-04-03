import chainlit as cl
from Agent import MyAgent
import asyncio
from agents import Runner , Agent


@cl.on_chat_start
async def chat_start():
    cl.user_session.set("history",[])
    await cl.Message("hello how can i help you today").send()
    
@cl.on_message
async def main(message: cl.Message):
    history = cl.user_session.get("history")
    Aimsg = cl.Message(content="")
    await Aimsg.send()

    user_query = message.content
    history.append({"role": "user", "content": user_query})
# streaming is supported
    response = Runner.run_streamed(
        starting_agent=asyncio.run(MyAgent()),
        input=history,
    )
    async for event in response.stream_events():
            if event.type == "raw_response_event" and hasattr(event.data, 'delta'):
                token = event.data.delta
                await Aimsg.stream_token(token)
    history.append({"role": "assistant", "content": Aimsg.content})
