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
