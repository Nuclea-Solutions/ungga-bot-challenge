import requests
import os
from dotenv import load_dotenv

load_dotenv()

rapidapi_key = os.environ["RAPID_API_KEY"]
url = "https://chatgpt-best-price.p.rapidapi.com/v1/chat/completions"

headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": rapidapi_key,
	"X-RapidAPI-Host": "chatgpt-best-price.p.rapidapi.com"
}
payload = {
	"model": "gpt-3.5-turbo",
	"messages": [
        {
            "role": "system",
            "content": "Eres un bot llamado Ungga Bot, tu mision principal es comprender la peticion del usuario para saber si necesita agendar una reunion o si necesita utilizar el servicio de traduccion, ten en cuenta que el servicio de agendamiento puede ser en multiples idiomas"
		},
        {
            "role": "assistant",
            "content": "Hola ! Soy Ungga Bot y estoy aqui para ayudarte, dime, que necesitas ?"
		},
	]
}

def result_to_rapidapi():
	response = requests.post(url, json=payload, headers=headers)
	result = response.json()
	print(result['choices'][0]['message']['content'])
	payload["messages"].append(result['choices'][0]['message'])

while True:
	print(payload['messages'])
	input_user = input('User: ').strip()

	if input_user == '':
		continue
	elif 'salir' in input_user:
		break
	else:
		payload["messages"].append({
			"role": "user",
			"content": input_user
		})
		result_to_rapidapi()

print(payload['messages'])
