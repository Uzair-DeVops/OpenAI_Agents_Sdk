from agents import Agent ,AsyncOpenAI,  Runner , set_tracing_disabled ,OpenAIChatCompletionsModel , RunConfig , set_default_openai_api , set_default_openai_client
from dotenv import load_dotenv 
import os

load_dotenv()

client = AsyncOpenAI(
        api_key=os.getenv("OPENROUTER_API_KEY"),
        base_url="https://openrouter.ai/api/v1",
)
# model = OpenAIChatCompletionsModel(
#     model ="shisa-ai/shisa-v2-llama3.3-70b:free",
#     openai_client = client
# )

set_default_openai_client(client)
set_default_openai_api("chat_completions")
set_tracing_disabled(True)


# Config = RunConfig(
#     model=model,
#     model_provider=client,
#     tracing_disabled=True,
# ) 



agent = Agent(
    name="Agent",
    instructions="You are a helpful assistant.",
    # model=model,
    model = "shisa-ai/shisa-v2-llama3.3-70b:free",
    )

response = Runner.run_sync(
    starting_agent=agent,
    input="What is the capital of France?",
    # run_config=Config,
)
print(response.final_output)