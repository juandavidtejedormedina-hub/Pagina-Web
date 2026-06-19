PAGE_HOME = "inicio"
PAGE_PROJECTS = "proyectos"
PAGE_LIBRARY = "biblioteca"

VALID_PAGES = {PAGE_HOME, PAGE_PROJECTS, PAGE_LIBRARY}

PROJECTS = [
    {
        "key": "bloques_sensores",
        "title": "Bloques y Sensores",
        "subtitle": "Finca Ponderosa",
        "description": (
            "Monitorea en tiempo real las variables ambientales de los "
            "invernaderos y prepara analisis de sensores para la finca."
        ),
        "icon": "greenhouse",
        "card_class": "project-card-primary",
        "library_class": "library-card-primary",
        "resources": 6,
    },
    {
        "key": "acrel",
        "title": "Acrel",
        "subtitle": "Monitoreo Electrico",
        "description": (
            "Visualiza el comportamiento electrico, consumos, alarmas y "
            "reportes del sistema Acrel en tiempo real."
        ),
        "icon": "bolt",
        "card_class": "project-card-acrel",
        "library_class": "library-card-acrel",
        "resources": 11,
    },
    {
        "key": "reservorios",
        "title": "Reservorios",
        "subtitle": "Gestion hidrica",
        "description": (
            "Consulta niveles, disponibilidad y seguimiento operativo de "
            "reservorios para apoyar decisiones de riego y mantenimiento."
        ),
        "icon": "droplet",
        "card_class": "project-card-reservoir",
        "library_class": "library-card-reservoir",
        "resources": 9,
    },
]

PROJECT_LABELS = {
    project["key"]: project["title"]
    for project in PROJECTS
}
