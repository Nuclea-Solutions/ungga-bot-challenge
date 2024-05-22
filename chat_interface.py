import gradio as gr
from app import chat_function

# Gradio graphic interface
gr.ChatInterface(
    chat_function,
    chatbot=gr.Chatbot(height=300),
    textbox=gr.Textbox(placeholder='Ask me anything', container=False, scale=7),
    title="Ungga Bot",
    description="I'm a bot that will help you to schedule appointments and help with translations",
    theme="soft",
    examples=["Hello, how are you?", "Can you schedule a meeting for tomorrow?", "Please, translate me this"],
    cache_examples=True,
    retry_btn=None,
    undo_btn="Delete Previous",
    clear_btn="Clear",
).launch()