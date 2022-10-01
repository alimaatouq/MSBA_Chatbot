import streamlit as st
from streamlit.components.v1 import html

st.write('<style>div.block-container{padding-top:0.5rem;}</style>', unsafe_allow_html=True)



# Define your javascript
my_js = """
alert("Hola mundo");
"""

# Wrapt the javascript as html code
my_html = f"<script>{my_js}</script>"

trial = """<script src="//code.tidio.co/29ahjkkgzjmufusyxfai4rhrqquki8xg.js" async></script>"""
# Execute your app
html(trial, width = 980, height=600)