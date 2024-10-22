import openai

api_key = "..."

openai.api_key = api_key


def askChatGPT(messages):
    MODEL = "gpt-3.5-turbo"
    response = openai.ChatCompletion.create(
        model=MODEL,
        messages=messages,
        temperature=1,
        max_tokens=1024)
    return response['choices'][0]['message']['content']


def single_response(str_input):
    return askChatGPT([{"role": "user", "content": str_input}])


def multi_response(str_in):
    messages = [{"role": "user", "content": ""}]
    text = ""
    for i in range(2):
        if i == 0:
            text = "以下的回答基于你对盾构机的知识, 你的回答需要不超过30个汉字，不多于2句话"
        if i == 1:
            text = str_in
        d = {"role": "user", "content": text}
        messages.append(d)

        text = askChatGPT(messages)
        d = {"role": "assistant", "content": text}
        # print('ChatGPT：' + text + '\n')
        messages.append(d)
    return text

# print(single_response("who are you?"))
