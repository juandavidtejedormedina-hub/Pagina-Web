from src.ui.assets import asset_data_uri


def app_styles() -> str:
    logo = asset_data_uri("login_logo_principal.png")
    watermark = asset_data_uri("login_flor_marca_agua.png")
    background = asset_data_uri("login_background_floral.jpg")

    greenhouse_bg = asset_data_uri("card_invernadero_watermark.png")
    tower_bg = asset_data_uri("card_torre_watermark.png")
    reservoir_bg = asset_data_uri("reservorios_fondo.png")

    return f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@500;600;700;800;900&display=swap');

    :root {{
        --elite-purple: #343472;
        --elite-purple-soft: #58559a;
        --elite-ink: #161d25;
        --elite-blue: #005fae;
        --elite-pink: #e780bd;
        --elite-sky: #d5eef8;
        --elite-mint: #e9f7f5;
        --elite-footer: #30346f;
        --sidebar-width: 304px;
        --footer-height: 44px;
        --font-main: 'Montserrat', 'Segoe UI', sans-serif;
    }}

    html, body, [data-testid="stAppViewContainer"], .stApp {{
        width: 100%;
        min-height: 100vh;
        background: #ffffff !important;
        font-family: var(--font-main);
    }}
    header[data-testid="stHeader"],
    section[data-testid="stSidebar"],
    [data-testid="stSidebarCollapsedControl"] {{
        display: none !important;
    }}
    [data-testid="stAppViewContainer"] > .main .block-container {{
        max-width: none !important;
        padding: 0 !important;
    }}
    .elite-shell, .elite-sidebar, .elite-main, .elite-footer {{
        box-sizing: border-box;
        font-family: var(--font-main);
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
        bottom: var(--footer-height);
        width: var(--sidebar-width);
        padding: 18px 28px 24px;
        color: #ffffff;
        background:
            radial-gradient(circle at 78% 18%, rgba(255,255,255,0.10), transparent 30%),
            radial-gradient(circle at 12% 80%, rgba(255,255,255,0.08), transparent 34%),
            linear-gradient(180deg, #58549a 0%, #3e3b80 48%, #30336c 100%);
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
    .elite-sidebar-logo {{
        width: 225px;
        height: 145px;
        margin: 0 auto 18px;
        display: flex;
        align-items: center;
        justify-content: center;
        position: relative;
        z-index: 2;
    }}
    .elite-sidebar-logo img {{
        width: 225px;
        height: auto;
        display: block;
    }}
    .elite-nav {{
        display: grid;
        gap: 8px;
        position: relative;
        z-index: 2;
    }}
    .elite-nav-link {{
        min-height: 58px;
        display: flex;
        align-items: center;
        gap: 16px;
        padding: 0 20px;
        border-radius: 8px;
        color: rgba(255,255,255,0.88);
        text-decoration: none;
        font-size: 1.04rem;
        font-weight: 700;
        transition: background 160ms ease, transform 160ms ease;
    }}
    .elite-nav-link:hover {{
        color: #ffffff;
        background: rgba(255,255,255,0.09);
        transform: translateX(1px);
    }}
    .elite-nav-link.is-active {{
        color: #ffffff;
        background: rgba(255,255,255,0.15);
        box-shadow: inset 0 1px 0 rgba(255,255,255,0.12);
    }}
    .elite-nav-icon {{
        width: 29px;
        height: 29px;
        flex: 0 0 29px;
    }}
    .elite-nav-icon svg {{
        width: 100%;
        height: 100%;
        stroke: currentColor;
        stroke-width: 1.85;
        fill: none;
        stroke-linecap: round;
        stroke-linejoin: round;
    }}
    .elite-main {{
        position: fixed;
        inset: 0 0 var(--footer-height) var(--sidebar-width);
        padding: clamp(30px, 4vh, 44px) clamp(28px, 4.6vw, 66px) 54px clamp(50px, 6.2vw, 88px);
        overflow-y: auto;
        isolation: isolate;
    }}
    .elite-main::before {{
        content: "";
        position: fixed;
        inset: 0 0 var(--footer-height) var(--sidebar-width);
        z-index: -2;
        background-image: url("{background}");
        background-size: cover;
        background-position: center right;
        background-repeat: no-repeat;
        filter: saturate(1.08) contrast(1.03);
    }}
    .elite-main::after {{
        content: "";
        position: fixed;
        inset: 0 0 var(--footer-height) var(--sidebar-width);
        z-index: -1;
        background:
            linear-gradient(90deg, rgba(255,255,255,0.94) 0%, rgba(255,255,255,0.58) 42%, rgba(255,255,255,0.03) 100%),
            radial-gradient(circle at 32% 40%, rgba(255,255,255,0.22), transparent 44%);
    }}
    .elite-footer {{
        position: fixed;
        left: 0;
        right: 0;
        bottom: 0;
        height: var(--footer-height);
        display: flex;
        align-items: center;
        justify-content: center;
        background: var(--elite-footer);
        color: #ffffff;
        z-index: 1001;
        font-size: 0.78rem;
        font-weight: 900;
        letter-spacing: 0.18em;
        text-transform: uppercase;
    }}
    .home-shell {{
        max-width: 1090px;
        min-height: calc(100vh - var(--footer-height) - 96px);
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
    .home-kicker, .library-kicker {{
        margin: 0 0 30px;
        color: #14146a;
        font-size: 0.98rem;
        font-weight: 800;
    }}
    .home-title, .library-title {{
        margin: 0;
        color: var(--elite-ink);
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
    .home-accent, .library-accent {{
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
        width: min(980px, calc(100vw - var(--sidebar-width) - 120px));
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
    .projects-shell {{
        min-height: calc(100vh - var(--footer-height) - 96px);
        display: flex;
        align-items: center;
        justify-content: center;
    }}
    .project-grid {{
        width: min(976px, 100%);
        display: grid;
        grid-template-columns: repeat(3, minmax(0, 1fr));
        gap: 30px;
    }}
    .project-card {{
        position: relative;
        min-height: 384px;
        border-radius: 10px;
        padding: 58px 36px 30px;
        overflow: hidden;
        border: 1px solid rgba(255,255,255,0.8);
        box-shadow: 0 22px 56px rgba(37,42,80,0.15);
    }}
    .project-card::after {{
        content: "";
        position: absolute;
        right: -8px;
        bottom: -6px;
        width: 190px;
        height: 160px;
        background-repeat: no-repeat;
        background-size: contain;
        background-position: right bottom;
        opacity: 0.22;
    }}
    .project-card-primary {{
        color: #ffffff;
        background: linear-gradient(145deg, #4e4a98 0%, #3b397d 100%);
    }}
    .project-card-primary::after {{
        background-image: url("{greenhouse_bg}");
        opacity: 0.18;
    }}
    .project-card-acrel {{
        color: #27256f;
        background: linear-gradient(145deg, rgba(220,241,250,0.96), rgba(192,229,246,0.94));
    }}
    .project-card-acrel::after {{
        background-image: url("{tower_bg}");
        opacity: 0.32;
    }}
    .project-card-reservoir {{
        color: #26246c;
        background: linear-gradient(145deg, rgba(238,251,249,0.98), rgba(218,241,239,0.94));
    }}
    .project-card-reservoir::after {{
        background-image: url("{reservoir_bg}");
        opacity: 0.24;
    }}
    .project-heading {{
        display: flex;
        align-items: center;
        gap: 24px;
        min-height: 84px;
    }}
    .project-icon {{
        width: 75px;
        height: 75px;
        flex: 0 0 75px;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        border-radius: 999px;
        color: currentColor;
        background: rgba(255,255,255,0.80);
        box-shadow: 0 3px 0 rgba(255,255,255,0.80), 0 12px 22px rgba(55,54,110,0.12);
    }}
    .project-card-primary .project-icon {{
        background: rgba(255,255,255,0.10);
        border: 1px solid rgba(255,255,255,0.24);
    }}
    .project-icon img {{
        width: 72px;
        height: 72px;
        object-fit: contain;
    }}
    .project-icon svg {{
        width: 42px;
        height: 42px;
        stroke: currentColor;
        stroke-width: 1.8;
        fill: none;
        stroke-linecap: round;
        stroke-linejoin: round;
    }}
    .project-title {{
        margin: 0;
        font-size: 1.55rem;
        line-height: 1.08;
        font-weight: 900;
    }}
    .project-title span {{
        display: block;
    }}
    .project-subtitle {{
        margin-top: 10px;
        display: block;
        color: #ee9ac7;
        font-size: 1rem;
        font-weight: 800;
    }}
    .project-card-reservoir .project-subtitle {{
        color: #5e9daf;
    }}
    .project-divider {{
        height: 1px;
        margin: 36px 0 20px;
        background: currentColor;
        opacity: 0.32;
    }}
    .project-copy {{
        min-height: 92px;
        margin: 0;
        font-size: 0.88rem;
        font-weight: 700;
        line-height: 1.58;
    }}
    .project-card-acrel .project-copy,
    .project-card-reservoir .project-copy {{
        color: #20276b;
        font-weight: 600;
    }}
    .project-action {{
        position: relative;
        z-index: 2;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        gap: 18px;
        min-height: 50px;
        margin-top: 10px;
        padding: 0 16px 0 10px;
        border-radius: 999px;
        text-decoration: none;
        white-space: nowrap;
        font-size: 0.88rem;
        font-weight: 900;
        color: #005fae;
        background: rgba(255,255,255,0.96);
    }}
    .project-card-acrel .project-action,
    .project-card-reservoir .project-action {{
        color: #ffffff;
        background: linear-gradient(90deg, #44398b, #2c3677);
    }}
    .project-card-reservoir .project-action {{
        background: linear-gradient(90deg, #315d87, #2f3378);
    }}
    .project-action svg {{
        width: 22px;
        height: 22px;
        stroke: currentColor;
        stroke-width: 2.1;
        fill: none;
    }}
    .library-shell {{
        max-width: 980px;
        padding-bottom: 72px;
    }}
    .library-kicker {{
        margin-bottom: 28px;
    }}
    .library-title {{
        color: #2d287d;
    }}
    .library-copy {{
        margin: 20px 0 0;
        color: #101469;
        font-size: 1rem;
        font-weight: 800;
    }}
    .library-accent {{
        margin-top: 16px;
    }}
    .library-summary {{
        display: grid;
        grid-template-columns: repeat(3, minmax(0, 1fr));
        gap: 12px;
        margin: 14px 0 30px;
    }}
    .summary-card {{
        min-height: 78px;
        padding: 16px 18px;
        border-radius: 9px;
        background: rgba(255,255,255,0.82);
        box-shadow: 0 18px 42px rgba(45,48,64,0.08);
    }}
    .summary-card strong {{
        display: block;
        color: #2d287d;
        font-size: 1.62rem;
        line-height: 1;
        font-weight: 900;
    }}
    .summary-card span {{
        display: block;
        margin-top: 8px;
        color: rgba(45,40,125,0.72);
        font-size: 0.76rem;
        font-weight: 900;
        text-transform: uppercase;
    }}
    .library-section-title {{
        margin: 0 0 30px;
        color: var(--elite-ink);
        font-size: 2rem;
        font-weight: 900;
        letter-spacing: 0;
    }}
    .library-grid {{
        display: grid;
        grid-template-columns: repeat(3, minmax(0, 1fr));
        gap: 20px;
    }}
    .library-card {{
        position: relative;
        min-height: 310px;
        border-radius: 10px;
        padding: 34px 22px 20px;
        overflow: hidden;
        text-decoration: none;
        border: 1px solid rgba(255,255,255,0.78);
        box-shadow: 0 20px 48px rgba(45,48,64,0.10);
    }}
    .library-card::after {{
        content: "";
        position: absolute;
        right: -8px;
        bottom: -8px;
        width: 190px;
        height: 145px;
        background-repeat: no-repeat;
        background-size: contain;
        background-position: right bottom;
        opacity: 0.22;
    }}
    .library-card-primary {{
        color: #ffffff;
        background: linear-gradient(145deg, #4d4995 0%, #3a397d 100%);
    }}
    .library-card-primary::after {{ background-image: url("{greenhouse_bg}"); }}
    .library-card-acrel {{
        color: #005fae;
        background: linear-gradient(145deg, rgba(220,241,250,0.96), rgba(196,230,246,0.94));
    }}
    .library-card-acrel::after {{ background-image: url("{tower_bg}"); opacity: 0.30; }}
    .library-card-reservoir {{
        color: #005fae;
        background: linear-gradient(145deg, rgba(238,251,249,0.98), rgba(218,241,239,0.94));
    }}
    .library-card-reservoir::after {{ background-image: url("{reservoir_bg}"); opacity: 0.24; }}
    .library-card-head {{
        display: flex;
        align-items: center;
        gap: 26px;
    }}
    .library-title-card {{
        margin: 0;
        font-size: 2.05rem;
        line-height: 1.14;
        font-weight: 900;
        text-decoration: underline;
        text-decoration-thickness: 3px;
        text-underline-offset: 4px;
    }}
    .library-subtitle-card {{
        display: block;
        margin-top: 12px;
        color: #ee80bf;
        font-size: 1.4rem;
        line-height: 1.2;
        font-weight: 900;
    }}
    .library-card-reservoir .library-subtitle-card {{
        color: #5e9daf;
    }}
    .library-meta {{
        position: absolute;
        left: 24px;
        bottom: 24px;
        display: inline-flex;
        align-items: center;
        gap: 10px;
        color: #005fae;
        font-size: 0.78rem;
        font-weight: 900;
        text-decoration: underline;
    }}
    .library-card-primary .library-meta {{
        color: #0070c8;
    }}
    .library-meta svg {{
        width: 19px;
        height: 19px;
        stroke: currentColor;
        stroke-width: 2;
        fill: none;
    }}
    .placeholder-shell {{
        max-width: 880px;
        min-height: calc(100vh - var(--footer-height) - 96px);
        display: flex;
        align-items: center;
    }}
    .placeholder-card {{
        width: min(760px, 100%);
        padding: 42px 46px;
        border-radius: 14px;
        background: rgba(255,255,255,0.82);
        box-shadow: 0 28px 70px rgba(43,48,79,0.13);
        backdrop-filter: blur(8px);
    }}
    .placeholder-kicker {{
        margin: 0 0 14px;
        color: #2d287d;
        font-size: 0.84rem;
        font-weight: 900;
        letter-spacing: 0.1em;
        text-transform: uppercase;
    }}
    .placeholder-title {{
        margin: 0;
        color: var(--elite-ink);
        font-size: 2.25rem;
        font-weight: 900;
    }}
    .placeholder-copy {{
        margin: 18px 0 26px;
        color: #20276b;
        font-size: 1rem;
        line-height: 1.65;
        font-weight: 600;
    }}
    .placeholder-action {{
        display: inline-flex;
        align-items: center;
        justify-content: center;
        min-height: 46px;
        padding: 0 22px;
        border-radius: 999px;
        background: #343472;
        color: #ffffff;
        text-decoration: none;
        font-weight: 900;
    }}
    @media (max-width: 1100px) {{
        :root {{ --sidebar-width: 276px; }}
        .project-grid, .library-grid {{ grid-template-columns: 1fr; max-width: 420px; }}
        .projects-shell {{ align-items: flex-start; }}
        .home-header {{ grid-template-columns: 1fr; }}
        .home-brand {{ display: none; }}
        .library-summary {{ grid-template-columns: 1fr; }}
    }}
    @media (max-width: 760px) {{
        :root {{ --sidebar-width: 0px; }}
        .elite-sidebar {{ display: none; }}
        .elite-main {{ left: 0; padding: 24px 18px 64px; }}
        .elite-main::before, .elite-main::after {{ left: 0; }}
        .elite-footer {{ font-size: 0.58rem; letter-spacing: 0.08em; }}
        .home-intro {{ width: 100%; }}
        .home-panel {{ height: 220px; }}
    }}
    </style>
    """
