from langchain_core.prompts import PromptTemplate
from langchain_core.prompts import FewShotPromptTemplate
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms.tongyi import Tongyi
from langchain_community.chat_models.tongyi import ChatTongyi

"""
PromptTemplate -&gt; StringPromptTemplate -&gt; BasePromptTemplate -&gt; RunnableSerializable -&gt; Runnable
FewShotPromptTemplate -&gt; StringPromptTemplate -&gt; BasePromptTemplate  -&gt; RunnableSerializable -&gt; Runnable
ChatPromptTemplate -&gt; BaseChatPromptTemplate -&gt; BasePromptTemplate  -&gt; RunnableSerializable -&gt; Runnable
Tongyi -&gt; BaseLLM -&gt; BaseLanguageModel -&gt; RunnableSerializable -&gt; Runnable
ChatTongyi -&gt; BaseChatModel -&gt; BaseLanguageModel -&gt; RunnableSerializable -&gt; Runnable
"""


template = PromptTemplate.from_template("我的邻居是：{lastname}，最喜欢：{hobby}")

res = template.format(lastname="张大明", hobby="钓鱼")
print(res, type(res))


res2 = template.invoke({"lastname": "周杰轮", "hobby": "唱歌"})
print(res2, type(res2))
