# Ungga challenge bot

![image](https://raw.githubusercontent.com/fazdevelop/fazdevelop/main/bot-imagen.png)

Simple bot using OPENAI (chatgpt-3.5) via Rapid API. I tried to use Langgraph and Langchain with OpenAi llm but I was limited because you need to pay for the use of the model. 

## How to use

1. Clone this repository.

2. Go to the directory:
    ```
    cd ungga-bot-challenge
    ```

3. I recommend using a virtual environment:
    ```bash
    python -m venv venv
    ```

4. Now, we need to activate the virtual environment
    ## git bash
    ```
    source venv/Script/activate
    ```
    ## powershell
    ```
    .\venv\Scripts\activate
    ```

5. Install project dependencies
    ```bash
    pip install -r requirements.txt
    ```
   >**NOTE: It may take some time**

6. Now, you have to create a .ENV file with the following configurations:
    ```
    RAPID_API_KEY=example
    DB_USER=example
    DB_PASSWORD=example
    DB_HOST=example
    DB_NAME=example
    ```
   >**NOTE: db functions do not work**

7. Finally. Execute the bot, it will be running by default in [localhost](http://127.0.0.1:7860).
    ```
    py chat_interface.py
    ```

## Technologies Used

  * Python
  * MySQL
  * Gradio
  * OpenAI
  * RapidAPI
