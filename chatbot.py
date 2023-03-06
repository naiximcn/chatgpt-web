import os
import openai

def chat(prompt):
    openai.api_key = "想屁吃" #在这里替换你的API 如果没有去https://platform.openai.com/account/api-keys新建一个 注意：切勿泄露你的API 只建议在本地填入API
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        prompt=prompt,
        temperature=0.7,
        max_tokens=2500,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
    )
    answer = response["choices"][0]["text"].strip()
    if len(answer) != 0:
        return answer
    else:
        return "ERROR ChatGPT不想回答你的问题" #没有收到消息的回答
