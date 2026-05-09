from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.prompts import ChatPromptTemplate
import os

# 使用 ChatPromptTemplate（更适合聊天模型）
prompt_template = ChatPromptTemplate.from_template(
    "我的邻居姓{lastname}，刚生了{gender}，你帮我起个名字，简单回答"
)

# 改用 ChatTongyi
model = ChatTongyi(model="qwen-max")

chain = prompt_template | model

res = chain.invoke({"lastname": "过", "gender": "女儿"})
print(res.content)  # Chat 模型返回的是 AIMessage，需要 .content 取文本