import streamlit as st
from streamlit_timeline import timeline
#import streamlit.components.v1 as components

from constants import *

st.set_page_config(page_title='DS - portfolio', layout="wide", page_icon='👨‍🔬')

#with st.sidebar:
#    components.html(linkedin_badge['linkedin'], height=300)
# st.sidebar.markdown(linkedin_badge['linkedin'],unsafe_allow_html=True)

# About Me section
st.subheader('Who Am I?')
st.write(info['Brief'])

st.subheader('Most interesting projects I have been involved with')
# with st.spinner(text="Building line"):
with open('timeline.json', "r") as f:
    data = f.read()

timeline(data, height=800)

st.sidebar.markdown('#### Contact me here :point_down: #### ')
st.sidebar.write('📧: schzpantoja@gmail.com')