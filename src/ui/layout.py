import streamlit as st

from src.config import PAGE_DASHBOARD, PAGE_HOME, PAGE_LIBRARY, PAGE_PROJECTS
from src.ui.assets import asset_data_uri
from src.ui.icons import icon
from src.ui.pages import render_dashboard_placeholder, render_home, render_library, render_projects
from src.ui.styles import app_styles


def _active_page(page: str) -> str:
    return PAGE_PROJECTS if page == PAGE_DASHBOARD else page


def _nav_link(page: str, label: str, icon_name: str, current_page: str) -> str:
    active = " is-active" if _active_page(current_page) == page else ""
    return (
        f'<a class="elite-nav-link{active}" href="?seccion={page}" target="_self">'
        f'<span class="elite-nav-icon">{icon(icon_name)}</span>'
        f'<span>{label}</span>'
        '</a>'
    )


def _page_html(page: str, project: str, library_project: str) -> str:
    if page == PAGE_PROJECTS:
        return render_projects()
    if page == PAGE_LIBRARY:
        return render_library()
    if page == PAGE_DASHBOARD:
        return render_dashboard_placeholder(project)
    return render_home()


def render_shell(current_page: str, current_project: str = "", library_project: str = "") -> None:
    logo = asset_data_uri("login_logo_principal.png")
    logo_html = f'<img src="{logo}" alt="The Elite Flower">' if logo else ""

    nav = "\n".join(
        [
            _nav_link(PAGE_HOME, "Inicio", "home", current_page),
            _nav_link(PAGE_PROJECTS, "Proyectos", "grid", current_page),
            _nav_link(PAGE_LIBRARY, "Biblioteca", "book", current_page),
        ]
    )

    html = f"""
    {app_styles()}
    <div class="elite-shell">
        <aside class="elite-sidebar">
            <div class="elite-sidebar-logo">{logo_html}</div>
            <nav class="elite-nav">{nav}</nav>
        </aside>
        <main class="elite-main">
            {_page_html(current_page, current_project, library_project)}
        </main>
        <footer class="elite-footer">The Elite Flower - Cultivamos excelencia, cosechamos futuro</footer>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)
