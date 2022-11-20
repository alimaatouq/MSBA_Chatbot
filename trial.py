import streamlit as st
from streamlit.components.v1 import html
import hydralit_components as hc

st.set_page_config(layout="wide", page_icon= "🤖")
st.write('<style>div.block-container{padding-top:0.5rem;}</style>', unsafe_allow_html=True)

over_theme = {'txc_inactive': 'white','menu_background':'#ECE4F5', 'option_active':'white'}

menu_data = [
    {'label': "Counties", 'icon': 'bi bi-bar-chart-line'},
    {'label': 'California', 'icon': '🇺🇸'},
    {'label': 'Vaccines', 'icon': '💉'},
    {'label': 'Health Equity', 'icon': '⚖️'},
    {'label':"Overview", 'icon':'🔍'}]

menu_id = hc.nav_bar( menu_definition=menu_data,
                     override_theme=over_theme,
    hide_streamlit_markers=True,
    sticky_nav=True, #at the top or not
    sticky_mode='sticky', #jumpy or not-jumpy, but sticky or pinned
)

def get_base64_of_bin_file(bin_file):
    """
    function to read png file
    ----------
    bin_file: png -> the background image in local folder
    """
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_bg_hack_url():
    '''
    A function to unpack an image from url and set as bg.
    Returns
    -------
    The background.
    '''

st.markdown(
    f"""
    <style>
    .stApp {{
    background: url("https://img.rawpixel.com/s3fs-private/rawpixel_images/website_content/v960-ning-30.jpg?w=800&dpr=1&fit=default&crop=default&q=65&vib=3&con=3&usm=15&bg=F4F4F3&ixlib=js-2.2.1&s=63dd5f402645ef52fb7dfb592aec765a");
    background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
)

set_bg_hack_url()

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

col1, col2, col3 = st.columns([1, 2, 1])

trial = """<script src="//code.tidio.co/29ahjkkgzjmufusyxfai4rhrqquki8xg.js" async></script>"""

with col2:
  # Execute your app
  html(trial, height=600)
  
with col1:
  st.markdown("<h1 style='color: #1e54e4;'>Your MSBA Assistant is a click away!</h1>", unsafe_allow_html=True)
  st.image("chat-bot-42.png")
 
with col3:
  st.markdown("<h1 style='color: #1e54e4;'>Made by MSBA Students for MSBA Students!</h1>", unsafe_allow_html=True)
