import html

from src.config import PAGE_DASHBOARD, PAGE_PROJECTS, PROJECT_LABELS, PROJECTS
from src.ui.assets import asset_data_uri
from src.ui.icons import icon


def _project_icon_html(project: dict) -> str:
    if project["key"] == "bloques_sensores":
        uri = asset_data_uri("card_icon_invernadero.png")
    elif project["key"] == "acrel":
        uri = asset_data_uri("card_icon_rayo.png")
    else:
        uri = ""

    if uri:
        return f'<img src="{uri}" alt="">'
    return icon(project["icon"])


def render_home() -> str:
    brand = asset_data_uri("login_brand_logo_transparent.png")
    brand_html = f'<img src="{brand}" alt="The Elite Flower">' if brand else ""
    return f"""
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
            <div class="home-brand">{brand_html}</div>
        </header>
        <div class="home-intro">
            <p class="home-copy">
                En esta p&aacute;gina podr&aacute;s ver y consultar algunos proyectos
                realizados en el &aacute;rea de <strong>automatizaci&oacute;n</strong>.
            </p>
            <div class="creator-pill">
                <span class="creator-icon">{icon("user")}</span>
                <span>Creador: <strong>Juan David Tejedor</strong></span>
            </div>
            <div class="home-panel"></div>
        </div>
    </section>
    """


def render_projects() -> str:
    cards = []
    for project in PROJECTS:
        title_lines = "".join(f"<span>{html.escape(part)}</span>" for part in project["title"].split(" y "))
        if project["key"] == "bloques_sensores":
            title_lines = "<span>Bloques y</span><span>Sensores</span>"
        href = f"?seccion={PAGE_DASHBOARD}&proyecto={project['key']}"
        cards.append(
            f"""
            <article class="project-card {project['card_class']}">
                <div class="project-heading">
                    <span class="project-icon">{_project_icon_html(project)}</span>
                    <h2 class="project-title">
                        {title_lines}
                        <span class="project-subtitle">{html.escape(project['subtitle'])}</span>
                    </h2>
                </div>
                <div class="project-divider"></div>
                <p class="project-copy">{html.escape(project['description'])}</p>
                <a class="project-action" href="{href}" target="_self">
                    <span>Ingresar al Dashboard</span>
                    {icon("arrow-right")}
                </a>
            </article>
            """
        )
    return f"""
    <section class="projects-shell">
        <div class="project-grid">
            {''.join(cards)}
        </div>
    </section>
    """


def render_library() -> str:
    total_docs = sum(project["resources"] for project in PROJECTS)
    cards = []
    for project in PROJECTS:
        title = project["title"]
        if project["key"] == "bloques_sensores":
            title_html = "Bloques y<br>Sensores"
            subtitle = "Finca<br>Ponderosa"
        else:
            title_html = html.escape(title)
            subtitle = html.escape(project["subtitle"])
        cards.append(
            f"""
            <a class="library-card {project['library_class']}" href="?seccion=biblioteca&biblioteca={project['key']}" target="_self">
                <div class="library-card-head">
                    <span class="project-icon">{_project_icon_html(project)}</span>
                    <h2 class="library-title-card">
                        {title_html}
                        <span class="library-subtitle-card">{subtitle}</span>
                    </h2>
                </div>
                <span class="library-meta">
                    {icon("book-open")}
                    <span>{project['resources']} recursos</span>
                </span>
            </a>
            """
        )

    return f"""
    <section class="library-shell">
        <header class="library-header">
            <p class="library-kicker">Bienvenido al &aacute;rea de</p>
            <h1 class="library-title">Biblioteca</h1>
            <p class="library-copy">Recursos, documentos y referencias t&eacute;cnicas</p>
            <div class="library-accent"></div>
        </header>
        <div class="library-summary">
            <div class="summary-card"><strong>{total_docs}</strong><span>Documentos disponibles</span></div>
            <div class="summary-card"><strong>{len(PROJECTS)}</strong><span>Proyectos organizados</span></div>
            <div class="summary-card"><strong>{len(PROJECTS)}</strong><span>Carpetas con recursos</span></div>
        </div>
        <h2 class="library-section-title">Explora por proyecto</h2>
        <div class="library-grid">
            {''.join(cards)}
        </div>
    </section>
    """


def render_dashboard_placeholder(project_key: str) -> str:
    project_name = PROJECT_LABELS.get(project_key, "Proyecto")
    return f"""
    <section class="placeholder-shell">
        <div class="placeholder-card">
            <p class="placeholder-kicker">Dashboard en construcci&oacute;n</p>
            <h1 class="placeholder-title">{html.escape(project_name)}</h1>
            <p class="placeholder-copy">
                El inicio y la navegaci&oacute;n ya est&aacute;n listos. Esta secci&oacute;n se conectar&aacute;
                despu&eacute;s con los datos, gr&aacute;ficas y an&aacute;lisis del proyecto.
            </p>
            <a class="placeholder-action" href="?seccion={PAGE_PROJECTS}" target="_self">Volver a proyectos</a>
        </div>
    </section>
    """
