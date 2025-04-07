from agents import Agent, Runner , OpenAIChatCompletionsModel , AsyncOpenAI , set_tracing_disabled
from dotenv import load_dotenv
import os
load_dotenv()

set_tracing_disabled(disabled=True)

provider = AsyncOpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model = "gemini-2.0-flash-exp",
    openai_client = provider,
)


def run():
    agent = Agent(
        name="Assistant", 
        instructions="You are a helpful assistant",
        model = model,
        )

    result = Runner.run_sync(agent, "tell me about Pakistan.")
    print(result.final_output)

run()
