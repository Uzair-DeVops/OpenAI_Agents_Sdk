from agents import Agent , Runner , set_tracing_disabled
import os
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig
import asyncio



set_tracing_disabled(True)

load_dotenv()
external_client = AsyncOpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

async def AIagent(user_query):
    agent = Agent(
        name="Assistant",
        instructions="You are helpful Assistant.",
        model=model
    )

    result = await Runner.run(agent, user_query)
    return (result.final_output)

asyncio.run(AIagent("tell me about pakistan in 2 lines"))