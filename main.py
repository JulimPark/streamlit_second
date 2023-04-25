import streamlit as st
import pandas as pd
st.write("hello!~~bye!!!")
df = pd.DataFrame(pd.read_csv('./exam_data.csv'))
df1 = df['정답']

df1.to_csv('./test.csv',mode='w',index=None)
