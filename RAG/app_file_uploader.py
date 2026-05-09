import streamlit as st
import  time
from knowlegde_base import KnowledgeBaseService

# session_state就是一个字典
if "service" not in st.session_state:
    st.session_state["service"] = KnowledgeBaseService()

st.title("知识库更新服务")
uploader_file=st.file_uploader(
    "请上传TXT文件",
    type=['txt'],
    accept_multiple_files=False,   #仅接受一个文件的上传
)

if uploader_file is not None:
    file_name=uploader_file.name
    file_type=uploader_file.type
    file_size=uploader_file.size/1024#单位为kb

    st.subheader(f"文件名：{file_name}")
    st.write(f"格式：{file_type} | 大小：{file_size:.2f}KB")

    #内容
    text=uploader_file.getvalue().decode("utf-8")
    with st.spinner("载入知识库中。。。"):       # 在spinner内的代码执行过程中，会有一个转圈动画
        time.sleep(1)
        result = st.session_state["service"].upload_by_str(text, file_name)
        st.write(result)

