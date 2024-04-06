import streamlit as st # フロントエンドを扱うstreamlitの機能をインポート
from PIL import Image # 画像扱うための機能をインポート
import pytesseract # 外部OCRを扱うための機能をインポート
import platform # OSの判別するために、プラットフォームを読み込む機能をインポート


# それぞれのOSにインストールされるtesseractの場所を指定
if platform.system() == "Windows":
    pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
else:
    pytesseract.pytesseract.tesseract_cmd = r"/usr/local/bin/tesseract"

# 画像読み込みのための言語と言語のコードを変換するリストを設定
set_language_list = {
    "日本語" :"jpn",
    "英語" :"eng",
}

st.title("文字認識アプリ") # タイトル表示
set_language = st.selectbox("文字認識する言語を選んでください。",set_language_list.keys()) # 言語選択のためのリスト
file_upload = st.file_uploader("ここに文字認識したファイルをアップロードしてください。",type=["png","jpg"]) # tesseractが認識できるpngとjpgだけを許可するアップローダーの設置

# アップロードされたらfile_uploadがNoneではなくなるので、実行される
if (file_upload !=None):

    st.image(file_upload) # 画像分析する画像を表示



    # 画像の文字を読み込む
    txt = pytesseract.image_to_string(Image.open(file_upload), lang=set_language_list[set_language])
    st.write(txt) # 分析結果を表示

    st.write("感情分析の結果") # 案内表示
    from asari.api import Sonar # 文字から感情分析する機能をインポート
    sonar = Sonar() # Sonar()をsonarに代入
    res = sonar.ping(text=txt) # sonar.ping(text=分析したい文字)で感情分析リクエストし、結果をresに代入
    st.write(res["classes"]) # res["classes"]に結果が変えて来るので、これを表示
