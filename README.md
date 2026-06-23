# Pagina Web Tejedor

Base limpia para trabajar la pagina web en Streamlit.

La aplicacion quedo en blanco con un "Hola mundo" en `Pagina.py`. La interfaz
anterior fue retirada para empezar de nuevo desde una base sencilla.

Se conserva la parte de datos, procesamiento y documentacion tecnica:

- `Datos/`
- `procesamiento/`
- `docs/`

## Preparar el proyecto

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Ejecutar localmente

```powershell
.\run.ps1
```

O manualmente:

```powershell
.\.venv\Scripts\Activate.ps1
streamlit run Pagina.py
```

## Preparar datos

El Excel original se conserva en `Datos/Raw/`. Para generar los CSV limpios:

```powershell
.\.venv\Scripts\python.exe procesamiento\limpiar_datos.py
```

Los archivos procesados quedan en `Datos/Procesados/`.
La hoja `Analisis Apertura` se separa en dos salidas: una de aperturas en
metros y otra de areas calculadas en m2.

Tambien se generan reportes de calidad en `Datos/Reportes/` para revisar nulos,
duplicados exactos y duplicados por llaves de negocio antes de tomar decisiones
de limpieza mas fuertes. Los ceros validos, como radiacion `0` o porcentajes
`0`, se conservan.

Para generar variables derivadas con sentido analitico:

```powershell
.\.venv\Scripts\python.exe procesamiento\generar_variables.py
```

Los archivos con variables quedan en `Datos/Analiticos/`. Esta etapa no elimina
filas por tener rezagos o promedios faltantes; deja los nulos para que el
analisis estadistico decida como tratarlos.

Para preparar reportes base del analisis estadistico:

```powershell
.\.venv\Scripts\python.exe procesamiento\preparar_analisis_estadistico.py
```

Esto genera resumen de datasets, estadistica descriptiva numerica y categorica,
ademas de posibles outliers por IQR en `Datos/Reportes/`.

## Git y repositorio remoto

Repositorio esperado:

```text
https://github.com/juandavidtejedormedina-hub/Pagina-Web.git
```

Si `git` no aparece en una terminal ya abierta, cierra y vuelve a abrir PowerShell o VS Code para refrescar el `PATH`.

Para subir cambios:

```powershell
git add .
git commit -m "Describe el cambio"
git push
```
