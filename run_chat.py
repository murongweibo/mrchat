import time
from pychatgpt import OpenAI

from loguru import logger
import streamlit as st
email = st.secrets["email"]
password = st.secrets["password"]

# Manually set the token
#OpenAI.Auth.save_access_token(access_token="eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1UaEVOVUpHTkVNMVFURTRNMEZCTWpkQ05UZzVNRFUxUlRVd1FVSkRNRU13UmtGRVFrRXpSZyJ9.eyJodHRwczovL2FwaS5vcGVuYWkuY29tL3Byb2ZpbGUiOnsiZW1haWwiOiIxNTgxNDgxMDA2OUAxMzkuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImdlb2lwX2NvdW50cnkiOiJVUyJ9LCJodHRwczovL2FwaS5vcGVuYWkuY29tL2F1dGgiOnsidXNlcl9pZCI6InVzZXIta1RyT09OVXdIck5wQlp1ZkFGRmdsSWZXIn0sImlzcyI6Imh0dHBzOi8vYXV0aDAub3BlbmFpLmNvbS8iLCJzdWIiOiJhdXRoMHw2MzkyYzIyMjExODk3ODI0NGE5NDlmOWUiLCJhdWQiOlsiaHR0cHM6Ly9hcGkub3BlbmFpLmNvbS92MSIsImh0dHBzOi8vb3BlbmFpLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2NzA1ODgxMzgsImV4cCI6MTY3MDYzMTMzOCwiYXpwIjoiVGRKSWNiZTE2V29USHROOTVueXl3aDVFNHlPbzZJdEciLCJzY29wZSI6Im9wZW5pZCBlbWFpbCBwcm9maWxlIG1vZGVsLnJlYWQgbW9kZWwucmVxdWVzdCBvcmdhbml6YXRpb24ucmVhZCBvZmZsaW5lX2FjY2VzcyJ9.QF_wRKjV75tRFlZD2WPylkMUvlH1B0uUCSFFP2772Dxpk2NWsC6FbZUC6t3AJB81uM6r6whz1GEkRbHK1lPRPYnQq8hQWmUhSKOGEp40dLOZdEFTeVPAdRzmh_2zQSjHA7RjEVjm5daUT5vThRia9gQw3VKTAXdw0ZL6vH6vz62xdyEbYwGUgtEj_QwGDo4xsC6jYwrlgymlyuTGWJ3ziaplWOU0lsg8eJhMFQztenmpAEte9fcD_M-DpcYfIqEEO0ePVnoncXty7XCiYZVNhx58vnhPJ7-yxgDW8HWPqlaYUUKhvtXfZIyqykQJKyeNx8uF_etB7CttOn4rnwmFkQ", expiry=time.time() + 3600)

from pychatgpt import Chat
from pychatgpt import Chat, Options

options.chat_log = f"chat_log.txt"
options.id_log = f"id_log.txt"

# Initializing the chat class will automatically log you in, check access_tokens
chat = Chat(email=email, password=password, options = options) 
input_txt = st.text_area("请输入你的问题：")

if input_txt:
    logger.info(f"你的问题是：{input_txt}")
    logger.info(f"正在提问：")
    answer = chat.ask(input_txt)
    logger.info(f"你的答案是：{answer}")
    st.markdown(answer)
