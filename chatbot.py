import os
import openai

def chat(prompt):
    openai.api_key = "replace with your api key"
    response = openai.Completion.create(
        model="text-davinci-003",
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
        return "Error: ChatGPT didn't return any texts."
