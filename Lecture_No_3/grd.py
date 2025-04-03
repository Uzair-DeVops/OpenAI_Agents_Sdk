import gradio as gr
import asyncio
from Agent import AIagent
from chatbot import AIbot

def run_agent(user_query):
    response = asyncio.run(AIagent(user_query))
    return response

iface = gr.Interface(
    fn=run_agent,
    inputs=gr.Textbox(lines=2, placeholder="Write your message here..."),
    outputs="text",
    title="Chatbot",
    description="A simple chatbot powered by AIagent."
)

iface.launch(enable_queue=False)
