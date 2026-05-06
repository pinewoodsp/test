import streamlit as st

st.set_page_config(
    page_title="동작·관악구 역사적 명소 리플렛",
    page_icon="🗺️",
    layout="wide"
)

with open("index.html", "r", encoding="utf-8") as f:
    html_code = f.read()

st.components.v1.html(html_code, height=900, scrolling=True)
