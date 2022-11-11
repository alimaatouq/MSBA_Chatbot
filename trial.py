import streamlit as st
from streamlit.components.v1 import html

st.write('<style>div.block-container{padding-top:0.5rem;}</style>', unsafe_allow_html=True)

trial = """<script src="//code.tidio.co/29ahjkkgzjmufusyxfai4rhrqquki8xg.js" async></script>"""
# Execute your app
html(trial, height=600)
