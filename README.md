# Pagina Web

Portafolio personal creado con Streamlit.

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

Tambien se generan reportes de calidad en `Datos/Reportes/` para revisar nulos,
duplicados exactos y duplicados por llaves de negocio antes de tomar decisiones
de limpieza mas fuertes. Los ceros validos, como radiacion `0` o porcentajes
`0`, se conservan.

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
