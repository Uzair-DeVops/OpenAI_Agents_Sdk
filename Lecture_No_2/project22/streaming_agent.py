from agents import Agent , Runner ,OpenAIChatCompletionsModel , AsyncOpenAI ,set_tracing_disabled
from dotenv import load_dotenv
import os
from openai.types.responses import ResponseTextDeltaEvent

import asyncio
load_dotenv()
set_tracing_disabled(True)
provider = AsyncOpenAI(
        api_key = os.getenv("GEMINI_API_KEY"),
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
    )

# creating model
model = OpenAIChatCompletionsModel(
    model = "gemini-2.0-flash",
    openai_client = provider

)



# creating agent



async def main():
    MyAgent = Agent(name = "Assistant", instructions= "You will response to user query",model = model)
    result  = Runner.run_streamed(starting_agent = MyAgent, input = "TELL ME 10 JOKES",)
    async for event in result.stream_events():
        if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
            print(event.data.delta, end="", flush=True)
asyncio.run(main())



# running agent


# dict = {}

# async for x in dict.keys():