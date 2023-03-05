# chatgpt-bot
利用OpenAI的gpt3.5API实现网站ChatGpt

程序遵守MIT协议开源

## 安装与使用
### 需要
环境及库：[`python`](python.org/downloads/) `openai` `flask`

网络：~~你要会游泳~~ 能访问OpenAI

### 配置
* 在chatboy.py: openai.api_key 中更换自己的API   如果没有去[`OpenAI`](https://platform.openai.com/account/api-keys)新建一个 注意：切勿泄露你的API 只建议在本地填入API
- 在main.py: @app.route 中更换路径   可以随便瞎写一个地址防止别人用(bushi) 访问时IP:端口+这里的地址双个斜杠单个斜杠 e.g 127.0.0.1:7666/6/gpt.sb
- 在main.py: app.run 中更换绑定IP和端口   如需外网访问0.0.0.0即可 如只需本机访问就改成127.0.0.1
- 在chatboy.py: retun 中更换没有收到返回的回答
- 在index.html: 43、45行 中更改标题和运营信息

### 启动
打开终端 在文件夹目录下输入 `Python路径 main.py` 并回车

如果出现类似于以下内容则说明启动成功
```
 * Serving Flask app 'main'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:7666
Press CTRL+C to quit
```

### 使用
浏览器访问 `IP`:`端口`+`@app.route中的地址(双个斜杠单个斜杠)` e.g `127.0.0.1:7666/6/gpt.sb`

在输入框中输入问题按`发送`键发送
