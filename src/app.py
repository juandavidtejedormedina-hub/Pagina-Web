import streamlit as st

from src.config import PAGE_DASHBOARD, PAGE_HOME, VALID_PAGES
from src.ui.layout import render_shell


def _query_param(name: str, default: str) -> str:
    value = st.query_params.get(name, default)
    if isinstance(value, list):
        return value[0] if value else default
    return value


def run() -> None:
    st.set_page_config(
        page_title="The Elite Flower | Proyectos",
        page_icon=":briefcase:",
        layout="wide",
        initial_sidebar_state="collapsed",
    )

    page = _query_param("seccion", PAGE_HOME)
    project = _query_param("proyecto", "")
    library_project = _query_param("biblioteca", "")

    if page not in VALID_PAGES:
        page = PAGE_HOME

    render_shell(
        current_page=page,
        current_project=project,
        library_project=library_project,
    )
