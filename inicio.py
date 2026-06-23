import base64
from pathlib import Path
from textwrap import dedent

import streamlit as st


BASE_DIR = Path(__file__).resolve().parent
IMG_DIR = BASE_DIR / "Imagenes"


def _asset_data_uri(filename: str) -> str:
    path = IMG_DIR / filename
    suffix = path.suffix.lower().lstrip(".")
    mime = "jpeg" if suffix in {"jpg", "jpeg"} else suffix
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:image/{mime};base64,{encoded}"


def _icon_home() -> str:
    return """
    <svg viewBox="0 0 24 24" aria-hidden="true">
        <path d="M3 10.5 12 3l9 7.5"/>
        <path d="M5 10v10h5v-6h4v6h5V10"/>
    </svg>
    """


def _icon_grid() -> str:
    return """
    <svg viewBox="0 0 24 24" aria-hidden="true">
        <rect x="3" y="3" width="7" height="7" rx="1.5"/>
        <rect x="14" y="3" width="7" height="7" rx="1.5"/>
        <rect x="3" y="14" width="7" height="7" rx="1.5"/>
        <rect x="14" y="14" width="7" height="7" rx="1.5"/>
    </svg>
    """


def _icon_book() -> str:
    return """
    <svg viewBox="0 0 24 24" aria-hidden="true">
        <path d="M4 5.5A2.5 2.5 0 0 1 6.5 3H20v16H7a3 3 0 0 0-3 3Z"/>
        <path d="M4 5.5V22"/>
        <path d="M8 7h8"/>
        <path d="M8 11h7"/>
    </svg>
    """


def _menu_link(page: str, label: str, icon_html: str, current_page: str) -> str:
    active = " active" if current_page == page else ""
    return f"""
    <a class="menu-link{active}" href="?seccion={page}" target="_self">
        <span class="menu-icon">{icon_html}</span>
        <span>{label}</span>
    </a>
    """


def render_inicio() -> None:
    current_page = st.query_params.get("seccion", "inicio")
    logo = _asset_data_uri("login_logo_principal.png")
    background = _asset_data_uri("fondo-flores.png")
    watermark = _asset_data_uri("login_flor_marca_agua.png")

    html = dedent(
        f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@500;600;700;800;900&display=swap');

        .stApp {{
            background: #ffffff;
        }}

        header[data-testid="stHeader"],
        section[data-testid="stSidebar"],
        [data-testid="stSidebarCollapsedControl"] {{
            display: none;
        }}

        [data-testid="stAppViewContainer"] > .main .block-container {{
            max-width: none;
            padding: 0;
        }}

        .elite-shell,
        .elite-sidebar,
        .elite-content,
        .elite-footer {{
            box-sizing: border-box;
            font-family: "Montserrat", "Segoe UI", sans-serif;
        }}

        .elite-shell {{
            position: fixed;
            inset: 0;
            overflow: hidden;
            background: #ffffff;
            z-index: 999;
        }}

        .elite-sidebar {{
            position: fixed;
            left: 0;
            top: 0;
            bottom: 44px;
            width: 304px;
            padding: 18px 28px 24px;
            color: #ffffff;
            background:
                radial-gradient(circle at 78% 18%, rgba(255,255,255,0.10), transparent 30%),
                radial-gradient(circle at 12% 80%, rgba(255,255,255,0.08), transparent 34%),
                linear-gradient(180deg, #58549a 0%, #403d82 48%, #30336c 100%);
            box-shadow: 20px 0 58px rgba(47,51,108,0.24);
            overflow: hidden;
        }}

        .elite-sidebar::before {{
            content: "";
            position: absolute;
            left: 28px;
            right: 22px;
            bottom: 76px;
            height: 270px;
            opacity: 0.13;
            background-image: url("{watermark}");
            background-repeat: no-repeat;
            background-position: center bottom;
            background-size: 250px auto;
        }}

        .elite-sidebar::after {{
            content: "";
            position: absolute;
            left: 48px;
            right: 44px;
            bottom: 76px;
            height: 1px;
            background: rgba(255,255,255,0.50);
        }}

        .sidebar-logo {{
            width: 225px;
            height: 145px;
            margin: 0 auto 18px;
            display: flex;
            align-items: center;
            justify-content: center;
            position: relative;
            z-index: 2;
        }}

        .sidebar-logo img {{
            width: 225px;
            height: auto;
            display: block;
        }}

        .menu {{
            display: grid;
            gap: 8px;
            position: relative;
            z-index: 2;
        }}

        .menu-link {{
            min-height: 58px;
            display: flex;
            align-items: center;
            gap: 16px;
            padding: 0 20px;
            border-radius: 8px;
            color: rgba(255,255,255,0.88);
            text-decoration: none;
            font-size: 1.04rem;
            font-weight: 800;
            transition: background 160ms ease, transform 160ms ease;
        }}

        .menu-link:hover {{
            color: #ffffff;
            background: rgba(255,255,255,0.09);
            transform: translateX(1px);
        }}

        .menu-link.active {{
            color: #ffffff;
            background: rgba(255,255,255,0.15);
            box-shadow: inset 0 1px 0 rgba(255,255,255,0.12);
        }}

        .menu-icon {{
            width: 29px;
            height: 29px;
            flex: 0 0 29px;
        }}

        .menu-icon svg {{
            width: 100%;
            height: 100%;
            stroke: currentColor;
            stroke-width: 1.85;
            fill: none;
            stroke-linecap: round;
            stroke-linejoin: round;
        }}

        .elite-content {{
            position: fixed;
            inset: 0 0 44px 304px;
            padding: clamp(30px, 4vh, 44px) clamp(28px, 4.6vw, 66px) 54px clamp(50px, 6.2vw, 88px);
            overflow-y: auto;
            isolation: isolate;
        }}

        .elite-content::before {{
            content: "";
            position: fixed;
            inset: 0 0 44px 304px;
            z-index: -2;
            background-image: url("{background}");
            background-size: cover;
            background-position: center right;
            background-repeat: no-repeat;
            filter: saturate(1.08) contrast(1.03);
        }}

        .elite-content::after {{
            content: "";
            position: fixed;
            inset: 0 0 44px 304px;
            z-index: -1;
            background:
                linear-gradient(90deg, rgba(255,255,255,0.94) 0%, rgba(255,255,255,0.58) 42%, rgba(255,255,255,0.03) 100%),
                radial-gradient(circle at 32% 40%, rgba(255,255,255,0.22), transparent 44%);
        }}

        .home-shell {{
            max-width: 1090px;
            min-height: calc(100vh - 140px);
            display: grid;
            grid-template-rows: auto minmax(320px, 1fr);
            gap: clamp(12px, 1.7vh, 20px);
        }}

        .home-header {{
            display: grid;
            grid-template-columns: minmax(360px, 1fr) minmax(340px, 480px);
            align-items: start;
            gap: 28px;
        }}

        .home-kicker {{
            margin: 0 0 30px;
            color: #14146a;
            font-size: 0.98rem;
            font-weight: 800;
        }}

        .home-title {{
            margin: 0;
            color: #161d25;
            font-size: clamp(2.4rem, 4vw, 3.05rem);
            line-height: 0.98;
            letter-spacing: 0;
            font-weight: 900;
        }}

        .home-title-small {{
            display: block;
            margin-top: 14px;
            font-size: 1.08rem;
            line-height: 1.15;
            font-weight: 800;
        }}

        .home-accent {{
            width: 92px;
            height: 5px;
            margin-top: 84px;
            border-radius: 999px;
            background: #d78ad7;
        }}

        .home-brand {{
            min-height: 250px;
            display: flex;
            align-items: center;
            justify-content: flex-end;
            padding-top: 36px;
        }}

        .home-brand img {{
            width: min(420px, 100%);
            height: auto;
            display: block;
        }}

        .home-intro {{
            width: min(980px, calc(100vw - 424px));
            align-self: end;
        }}

        .home-copy {{
            max-width: 440px;
            margin: 0 0 14px;
            color: #101469;
            font-size: 1.02rem;
            font-weight: 600;
            line-height: 1.6;
        }}

        .creator-pill {{
            display: inline-flex;
            align-items: center;
            gap: 14px;
            min-height: 48px;
            padding: 0 24px 0 12px;
            border-radius: 999px;
            color: #2c2870;
            background: linear-gradient(90deg, rgba(220,207,255,0.88), rgba(241,231,255,0.82));
            font-size: 0.94rem;
            font-weight: 600;
        }}

        .creator-icon {{
            width: 38px;
            height: 38px;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            border-radius: 999px;
            color: #393286;
            background: rgba(198,177,255,0.72);
        }}

        .creator-icon svg {{
            width: 24px;
            height: 24px;
            stroke: currentColor;
            stroke-width: 1.8;
            fill: none;
        }}

        .home-panel {{
            height: clamp(260px, 42vh, 324px);
            margin-top: 20px;
            border-radius: 16px;
            background: rgba(255,255,255,0.78);
            border: 1px solid rgba(255,255,255,0.78);
            box-shadow: 0 28px 70px rgba(43,48,79,0.12);
            backdrop-filter: blur(8px);
        }}

        .elite-footer {{
            position: fixed;
            left: 0;
            right: 0;
            bottom: 0;
            height: 44px;
            display: flex;
            align-items: center;
            justify-content: center;
            background: #30346f;
            color: #ffffff;
            z-index: 1001;
            font-size: 0.78rem;
            font-weight: 900;
            letter-spacing: 0.18em;
            text-transform: uppercase;
        }}

        @media (max-width: 900px) {{
            .elite-sidebar {{
                width: 260px;
            }}

            .elite-content,
            .elite-content::before,
            .elite-content::after {{
                left: 260px;
            }}

            .home-brand {{
                display: none;
            }}

            .home-header {{
                grid-template-columns: 1fr;
            }}
        }}
        </style>

        <div class="elite-shell">
            <aside class="elite-sidebar">
                <div class="sidebar-logo">
                    <img src="{logo}" alt="The Elite Flower">
                </div>

                <nav class="menu">
                    {_menu_link("inicio", "Inicio", _icon_home(), current_page)}
                    {_menu_link("proyectos", "Proyectos", _icon_grid(), current_page)}
                    {_menu_link("biblioteca", "Biblioteca", _icon_book(), current_page)}
                </nav>
            </aside>

            <main class="elite-content">
                <section class="home-shell">
                    <header class="home-header">
                        <div>
                            <p class="home-kicker">Bienvenido al &aacute;rea de</p>
                            <h1 class="home-title">
                                Mantenimiento
                                <span class="home-title-small">Soporte El&eacute;ctrico y Automatizaci&oacute;n</span>
                            </h1>
                            <div class="home-accent"></div>
                        </div>
                        <div class="home-brand">
                            <img src="{logo}" alt="The Elite Flower">
                        </div>
                    </header>

                    <div class="home-intro">
                        <p class="home-copy">
                            En esta p&aacute;gina podr&aacute;s ver y consultar algunos proyectos
                            realizados en el &aacute;rea de <strong>automatizaci&oacute;n</strong>.
                        </p>
                        <div class="creator-pill">
                            <span class="creator-icon">{_icon_user()}</span>
                            <span>Creador: <strong>Juan David Tejedor</strong></span>
                        </div>
                        <div class="home-panel"></div>
                    </div>
                </section>
            </main>

            <footer class="elite-footer">
                The Elite Flower - Cultivamos excelencia, cosechamos futuro
            </footer>
        </div>
        """
    ).strip()

    if hasattr(st, "html"):
        st.html(html)
    else:
        st.markdown(html, unsafe_allow_html=True)


def _icon_user() -> str:
    return """
    <svg viewBox="0 0 24 24" aria-hidden="true">
        <circle cx="12" cy="8" r="4"/>
        <path d="M4 21c1.7-4 4.5-6 8-6s6.3 2 8 6"/>
    </svg>
    """
