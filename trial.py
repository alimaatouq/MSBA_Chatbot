import streamlit as st
from streamlit.components.v1 import html
import hydralit_components as hc

st.set_page_config(page_title="MSBA Assistant", layout="wide", page_icon= "🤖")

st.write('<style>div.block-container{padding-top:0rem;}</style>', unsafe_allow_html=True)


#edit footer
page_style= """
    <style>
    footer{
        visibility: visible;
        }
    footer:after{
        content: 'Developed by Ali Maatouk';
        display:block;
        position:relative;
        color:#1e54e4;
    }
    </style>"""

st.markdown(page_style, unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 1.5, 1])

trial = """<script src="//code.tidio.co/29ahjkkgzjmufusyxfai4rhrqquki8xg.js" async></script>"""

with col2:
  # Execute your app
  html(trial, height=600)
  
with col1:
  st.markdown("<h1 style='color: #1e54e4;'>Your MSBA Assistant is a click away!</h1>", unsafe_allow_html=True)
  st.image("chat-bot-42.png")
 
with col3:
  st.markdown("<h1 style='color: #1e54e4;'>Made by MSBA Students for MSBA Students!</h1>", unsafe_allow_html=True)
