import pandas as pd

import streamlit as st
from streamlit_timeline import timeline
#from streamlit_timeline import st_timeline

st.set_page_config(page_title='DS - portfolio', layout="wide", page_icon='👨‍🔬')

df = pd.DataFrame(
    {
        "name": ["Reino de Patones", "Mini Desafío la Morra"],
        "url": ["https://bramblesgroup.sharepoint.com/:i:/r/sites/SandBox953/Shared%20Documents/General/Orange%20White%20Green%20Neo%20Brutalism%20Business%20Performance%20Dashboard%20Graph.png?csf=1&web=1&e=JcWOm3", 
                "https://bramblesgroup.sharepoint.com/:i:/r/sites/SandBox953/Shared%20Documents/General/Orange%20White%20Green%20Neo%20Brutalism%20Business%20Performance%20Dashboard%20Graph.png?csf=1&web=1&e=JcWOm3"],
    }
)

st.dataframe(
    df,
    column_config={
        "name": "App name",
        "url": st.column_config.ImageColumn("Resume"),

    },
    hide_index=True,
)
# st.set_page_config(layout="wide")

# st.markdown('<meta http-equiv=”Content-Type” content=”text/html; charset=UTF-8″ />',unsafe_allow_html=True)

with open('./pages/races.json', "r") as f:
    data = f.read()
    timeline(data, height=800)


# items = [
#     {"id": 1, "content": "Reino de Patones", "start": "2024-02-25"},
#     {"id": 2, "content": "Mini Desafío La Morra", "start": "2024-03-10"},
# ]

#timeline = st_timeline(items, groups=[], options={}, height="300px")
#st.subheader("Selected item")
#st.write(timeline)