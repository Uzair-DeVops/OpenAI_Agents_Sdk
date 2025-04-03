from agents import Agent , Runner ,OpenAIChatCompletionsModel ,AsyncOpenAI ,set_tracing_disabled
from dotenv import load_dotenv
import os , asyncio

load_dotenv()

provider = AsyncOpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"

)

set_tracing_disabled(True)
model= OpenAIChatCompletionsModel(
    model = "gemini-2.0-flash-exp",
    openai_client=provider
)

async def MyAgent():
    agent = Agent(
        name="Assistant",
        instructions="you will respond to user query",
        model=model
    )

    # response = await Runner.run(agent,user_query)
    return agent


# print(asyncio.run(main("tell me about pakistan in 2 lines")))