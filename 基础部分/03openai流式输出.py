from openai import OpenAI

client=OpenAI(
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)
response=client.chat.completions.create(
    model="qwen3-max",
    messages=[
        {"role":"system","content":"你是一个python编程专家，并且话很多"},
        {"role":"assistant","content":"好的，我是编程专家并且话很多"},
        {"role":"user","content":"输出数字1-10，使用python代码"},
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