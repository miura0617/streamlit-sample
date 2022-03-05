from multiprocessing import Condition
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit超入門')

st.write('DataFrame')

df1 = pd.DataFrame({
    '1列名': [1, 2, 3, 4],
    '2列目': [40, 30, 20, 10]
})

# # 動的なテーブル
# st.dataframe(df1)
st.dataframe(df1.style.highlight_max())
# # 静的なテーブル
# st.table(df1.style.highlight_max(axis=0))

"""
マジックコマンドの使用例
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""


"""
チャートを書く

"""
df2 = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a', 'b', 'c']
)
# 折れ線グラフ
st.line_chart(df2)
# 積み重ねグラフ
st.area_chart(df2)
# 棒グラフ
st.bar_chart(df2)

"""
マップをプロット
東京の緯度(35.69, 139.70)
lat(緯度)、lon(経度)
"""
df3 = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns=["lat", "lon"]
)
st.map(df3)

"""
画像を表示
"""
st.write('Display Image')
img = Image.open('sample.png')
st.image(img, caption='sample image', use_column_width=True)

"""
インタラクティブなウィジェット
"""
st.write('インタラクティブなウィジェット')
# # チェックボックス
if st.checkbox('Show Image'):
    img = Image.open('sample.png')
    st.image(img, caption='sample image', use_column_width=True)

# # セレクトボックス
option = st.selectbox(
    'あなたが好きな数字を教えて下さい',
    list(range(1, 11))
)
st.write('あなたの好きな数字は、', option, 'です。')

# # テキストボックス
option = st.text_input('あなたの趣味を教えて下さい')
st.write('あなたの趣味：', option)

# # スライダー
condition = st.slider('あなたの今の調子は？', 0, 100, 50)
st.write('コンディション：', condition)

"""
プログレスバー
"""
