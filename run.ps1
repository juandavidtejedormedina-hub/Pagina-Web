$ErrorActionPreference = "Stop"

if (-not (Test-Path ".\.venv\Scripts\Activate.ps1")) {
    python -m venv .venv
}

.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
streamlit run Pagina.py
