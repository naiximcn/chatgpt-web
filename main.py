from flask import Flask, request, render_template
from chatbot import chat

app = Flask(__name__)


@app.route('//6//gpt.sb') #可以随便瞎写一个地址防止别人用(bushi) 访问时IP:端口+这里的地址双个斜杠单个斜杠 e.g 127.0.0.1:7666/6/gpt.cnm
def home():
    return render_template('index.html') #可以替换成在templates目录下的其他html


@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form['user_input']
    text = ""
    prompt = text + "\n" + user_input
    if len(prompt) <= 2000: #千万别改 OpenAI扣你钱了别怪我
        result = chat(prompt)
    else:
        result = chat(prompt[-2000:])
    return {'chatbot_response': result}


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=7666) #这里可以改IP端口 IP改为127.0.0.1就只能本机访问
