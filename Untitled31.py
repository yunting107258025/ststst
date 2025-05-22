#!/usr/bin/env python
# coding: utf-8

# In[10]:


import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title="APR Dashboard", layout="wide")

st.title("APR vs AP 分群互動圖（右偏分布）")

# 產生右偏分布資料
np.random.seed(42)
apr = np.random.lognormal(mean=2, sigma=0.5, size=6000)
ap = np.random.lognormal(mean=1.5, sigma=0.6, size=6000)
部 = np.random.choice(['A部', 'B部', 'C部'], size=6000)
客戶名稱 = [f"客戶{i+1}" for i in range(6000)]
size_clean = ap * 5000

df = pd.DataFrame({
    'APR': apr,
    'AP': ap,
    'size_clean': size_clean,
    '部': 部,
    '客戶名稱': 客戶名稱
})

# 畫互動圖
fig = px.scatter(
    df,
    x="APR",
    y="size_clean",
    color="部",
    hover_name="客戶名稱",
    size="size_clean",
    title="APR vs AP (右偏分布 + 部門分群)",
    height=600
)

st.plotly_chart(fig, use_container_width=True)


# In[ ]:




