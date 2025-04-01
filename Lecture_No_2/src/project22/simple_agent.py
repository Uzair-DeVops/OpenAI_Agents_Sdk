from agents import Agent , Runner ,OpenAIChatCompletionsModel , AsyncOpenAI ,set_tracing_disabled
from dotenv import load_dotenv
import os
load_dotenv()
set_tracing_disabled(True)
provider = AsyncOpenAI(
        api_key = os.getenv("GEMINI_API_KEY"),
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
    )

# creating model
model = OpenAIChatCompletionsModel(
    model = "gemini-2.0-flash-exp",
    openai_client = provider

)

# creating agent
MyAgent = Agent(
    name = "Assistant",
    instructions= "You will response to user query",
    model = model
)

# running agent
response  = Runner.run_sync(
    starting_agent = MyAgent,
    input = "Hello, how are you?",
)

print(response.final_output)