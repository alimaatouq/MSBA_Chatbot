import streamlit as st
from streamlit.components.v1 import html

st.write('<style>div.block-container{padding-top:0.5rem;}</style>', unsafe_allow_html=True)

col1, col2, col3 = st.columns([2, 4, 2])

trial = """<script src="//code.tidio.co/29ahjkkgzjmufusyxfai4rhrqquki8xg.js" async></script>"""

with col2:
  # Execute your app
  html(trial, height=600)
  
with col1:
  st.header("Your MSBA Assistant is a click away!")
