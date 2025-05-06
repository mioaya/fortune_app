import streamlit as st
import random

st.title("🔮 今日の運勢占い")

# 名前の入力
name = st.text_input("あなたの名前を入力してください")

if st.button("占う！"):
    fortunes = ["🌟 大吉", "😊 中吉", "😐 小吉", "😅 末吉", "💀 凶"]
    colors = ["赤", "青", "緑", "黄色", "紫", "ピンク", "オレンジ", "白", "黒"]
    advices = [
        "焦らずゆっくり進みましょう。",
        "今日は挑戦してみると吉！",
        "笑顔を忘れずに過ごしてね。",
        "新しいことに目を向けてみて。",
        "感謝の気持ちを大切に。",
        "無理せず休憩も大事。",
        "人との会話が幸運のカギ！"
    ]

    result = random.choice(fortunes)
    lucky_color = random.choice(colors)
    advice = random.choice(advices)

    st.write(f"{name}さんの今日の運勢は……")
    st.subheader(result)
    st.write(f"🎨 ラッキーカラー：{lucky_color}")
    st.write(f"💡 アドバイス：{advice}")
