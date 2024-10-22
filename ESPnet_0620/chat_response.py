import openai

api_key = "..."

openai.api_key = api_key


def askChatGPT(messages):
    MODEL = "gpt-3.5-turbo"
    response = openai.ChatCompletion.create(
        model=MODEL,
        messages=messages,
        temperature=1)
    return response['choices'][0]['message']['content']


def single_response(str_input):
    return askChatGPT([{"role": "user", "content": str_input}])

# print(single_response("who are you?"))
