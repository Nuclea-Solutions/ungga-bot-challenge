import requests
import os
import gradio as gr
from dotenv import load_dotenv

load_dotenv()

def chat_function(message, history):
	## rapid api setup
	rapidapi_key = os.environ["RAPID_API_KEY"]
	url = "https://chatgpt-best-price.p.rapidapi.com/v1/chat/completions"

	headers = {
		"content-type": "application/json",
		"X-RapidAPI-Key": rapidapi_key,
		"X-RapidAPI-Host": "chatgpt-best-price.p.rapidapi.com"
	}
	## Messsage history
	messages = [{"role": "system", "content": "Eres un bot llamado Ungga Bot, tu mision principal es comprender la peticion del usuario para saber si necesita agendar una reunion o si necesita utilizar el serviciode traduccion, ten en cuenta que el servicio de agendamiento puede ser en multiples idiomas"}]
	for user_input, bot_response in history:
		messages.append({"role": "user", "content": user_input})
		messages.append({"role": "assistant", "content": bot_response})
	messages.append({"role":"user","content":message})

	payload = {
		"model": "gpt-3.5-turbo",
		"messages": messages
	}

	## API request
	response = requests.post(url, json=payload, headers=headers)
	result = response.json()
	bot_response = result['choices'][0]['message']['content']

	return bot_response

gr.ChatInterface(
    chat_function,
    chatbot=gr.Chatbot(height=300),
    textbox=gr.Textbox(placeholder='Ask anything, if want to end type "quit" ', container=False, scale=7),
    title="Ungga Bot",
    description="I'm a bot that will help you to agend appointments",
    theme="soft",
    examples=["Hello", "Can you appointment a meeting?", "Please, translate me this"],
    cache_examples=True,
    retry_btn=None,
    undo_btn="Delete Previous",
    clear_btn="Clear",
).launch()