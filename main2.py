from multiprocessing import Condition
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image


"""
レイアウト(サイドバー)
"""
# # テキストボックスとスライダー
option = st.sidebar.text_input('あなたの趣味を教えて下さい')
condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)

st.write('あなたの趣味：', option)
st.write('コンディション：', condition)
