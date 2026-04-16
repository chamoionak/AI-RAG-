from openai import OpenAI

client=OpenAI(
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)
response=client.chat.completions.create(
    model="qwen3-max",
    messages=[
        {"role":"system","content":"你是一个AI助理，并且回答简洁"},
        {"role":"user","content":"小明有两条狗"},
        {"role":"assistant","content":"好的"},
        {"role":"user","content":"小红有三只猫"},
        {"role":"assistant","content":"好的"},
        {"role":"user","content":"总共有几只动物？"},
    ],
    stream=True
)
#print(response.choices[0].message.content)
for chunk in response:
    print(
        chunk.choices[0].delta.content,
        flush=True,#立即刷新缓冲区
        end=" "#每段之间以空格分割
          )