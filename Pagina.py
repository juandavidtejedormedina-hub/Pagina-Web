import streamlit as st

from inicio import render_inicio


st.set_page_config(
    page_title="Pagina Web Tejedor",
    layout="wide",
)

render_inicio()
