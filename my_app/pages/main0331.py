# streamlitのインポート
import streamlit as st

# テキストの表示
st.write("demoです")

# ボタンの表示
button = st.button("クリック")
if button:
    st.write("ボタンがクリックされました")

# 選択ボックス
options = st.multiselect(
    'どの寿司が好きですか',
    ['いか', 'えび', 'まぐろ', 'サーモン'],
    ["いか"])
st.write(",".join(options))




# git init
# git remote add origin https://github.com/jasminetech0/streamlit_training1.git
# git add .
# git commit -m'1st commit'
# git push origin main


# streamlit run main.py