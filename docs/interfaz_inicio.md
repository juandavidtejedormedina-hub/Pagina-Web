# Interfaz inicial Streamlit

Se reconstruyo el inicio de la pagina usando como referencia el proyecto
anterior ubicado en:

```text
C:\Users\pastautomatizacion4\OneDrive - Elite Flower\Escritorio\Dashboard Variables\dashboard_repo_limpio
```

La idea fue conservar la experiencia visual inicial y mejorar la estructura
del codigo para que no todo quede en un solo archivo.

## Que se conservo como guia

- Fondo floral.
- Barra lateral morada.
- Logo de The Elite Flower.
- Navegacion: Inicio, Proyectos y Biblioteca.
- Tarjetas de proyectos:
  - Bloques y Sensores
  - Acrel
  - Reservorios
- Tarjetas de biblioteca por proyecto.
- Botones de ingreso al dashboard.

## Que no se copio

- Logica vieja de dashboards.
- Carga antigua de datos.
- Filtros y graficas viejas.
- Codigo de Supabase.
- Estructura mezclada del proyecto anterior.

## Estructura nueva

```text
Pagina.py
src/
  app.py
  config.py
  assets/
  ui/
    assets.py
    icons.py
    layout.py
    pages.py
    styles.py
```

## Funcionamiento actual

Rutas principales:

```text
?seccion=inicio
?seccion=proyectos
?seccion=biblioteca
?seccion=dashboard&proyecto=bloques_sensores
?seccion=dashboard&proyecto=acrel
?seccion=dashboard&proyecto=reservorios
```

Por ahora, los botones de dashboard llevan a una pantalla placeholder. Mas
adelante conectaremos cada proyecto con sus datos, graficas y analisis.

## Proxima etapa

El siguiente paso sera empezar con el dashboard de **Bloques y Sensores** usando
los datos de `Datos/Analiticos/`.
