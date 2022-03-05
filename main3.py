import streamlit as st
import time

"""
レイアウト(2カラム)
"""

left_column, right_column = st.columns(2)

# 左側ボタン、右側テキスト
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラムです')


"""
Expander
"""
expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせ内容1を書く')
expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせ内容2を書く')
expander3 = st.expander('問い合わせ3')
expander3.write('問い合わせ内容3を書く')


"""
プログレスバー
"""
st.write('Start !!')
# 空要素を準備
latest_iteration = st.empty()

bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

"""
デプロイ（Webへ公開）
"""
st.write('1. streamlit sharingへ登録')
st.write('2. Gitを使う')
