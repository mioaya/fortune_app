import streamlit as st
import random

st.title("🔮 今日の運勢占い")

name = st.text_input("あなたの名前を入力してください")

if st.button("占う！"):
    fortunes = ["🌟 大吉", "😊 中吉", "😐 小吉", "😅 末吉", "💀 凶"]
    result = random.choice(fortunes)
    st.write(f"{name}さんの今日の運勢は……")
    st.subheader(result)
