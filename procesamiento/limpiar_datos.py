from __future__ import annotations

import re
import unicodedata
from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[1]
RAW_FILE = BASE_DIR / "Datos" / "Raw" / "Datos Excel.xlsx"
OUTPUT_DIR = BASE_DIR / "Datos" / "Procesados"


WIGGA_SHEETS = {
    "WIGGA bloque 38": "B38",
    "WIGGA bloque 27": "B27",
    "WIGGA bloque 35": "B35",
    "WIGGA bloque 34": "B34",
}

CORTINAS_SHEETS = {
    "Cortinas BLOQUE 38": "B38",
    "Cortinas BLOQUE 27": "B27",
    "Cortinas BLOQUE 35": "B35",
    "Cortinas BLOQUE 34": "B34",
}


def normalizar_columna(nombre: object) -> str:
    texto = str(nombre).strip().lower()
    texto = texto.replace("µ", "u")
    texto = unicodedata.normalize("NFKD", texto)
    texto = "".join(char for char in texto if not unicodedata.combining(char))
    texto = texto.replace("°", "")
    texto = re.sub(r"[^a-z0-9]+", "_", texto)
    texto = re.sub(r"_+", "_", texto).strip("_")
    return texto


def extraer_numero_bloque(codigo_bloque: str) -> str:
    return codigo_bloque.replace("B", "")


def limpiar_wigga() -> pd.DataFrame:
    tablas = []

    for hoja, bloque in WIGGA_SHEETS.items():
        df = pd.read_excel(RAW_FILE, sheet_name=hoja)
        df.columns = [normalizar_columna(col) for col in df.columns]

        bloque_numero = extraer_numero_bloque(bloque)
        rename_map = {}
        for col in df.columns:
            limpio = col.replace(f"_{bloque.lower()}_", "_")
            limpio = limpio.removesuffix(f"_{bloque.lower()}")
            limpio = limpio.replace(f"b{bloque_numero}", "")
            limpio = re.sub(r"_+", "_", limpio).strip("_")
            rename_map[col] = limpio

        df = df.rename(columns=rename_map)
        df["bloque"] = bloque
        df["fecha_hora"] = pd.to_datetime(
            df["fecha"].astype(str) + " " + df["hora"].astype(str),
            errors="coerce",
        )

        columnas_ordenadas = ["fecha_hora", "fecha", "hora", "bloque"]
        columnas_ordenadas += [col for col in df.columns if col not in columnas_ordenadas]
        df = df[columnas_ordenadas]
        tablas.append(df)

    wigga = pd.concat(tablas, ignore_index=True)
    wigga = wigga.drop_duplicates(subset=["fecha_hora", "bloque"])
    wigga = wigga.sort_values(["bloque", "fecha_hora"]).reset_index(drop=True)
    return wigga


def _limpiar_hora(valor: object) -> str | None:
    if pd.isna(valor):
        return None
    if hasattr(valor, "strftime"):
        return valor.strftime("%H:%M")
    texto = str(valor).strip()
    if not texto:
        return None
    return texto[:5]


def limpiar_cortinas() -> pd.DataFrame:
    registros = []

    for hoja, bloque in CORTINAS_SHEETS.items():
        raw = pd.read_excel(RAW_FILE, sheet_name=hoja, header=None)
        datos = raw.iloc[3:].copy()

        for _, row in datos.iterrows():
            fecha = pd.to_datetime(row.iloc[0], errors="coerce")
            if pd.isna(fecha):
                continue

            registros.append(
                {
                    "fecha": fecha.date().isoformat(),
                    "bloque": bloque,
                    "lado": "A",
                    "elemento": row.iloc[7],
                    "hora_apertura": _limpiar_hora(row.iloc[1]),
                    "porcentaje_apertura": pd.to_numeric(row.iloc[2], errors="coerce"),
                    "duracion_apertura_min": pd.to_numeric(row.iloc[3], errors="coerce"),
                    "hora_cierre": _limpiar_hora(row.iloc[4]),
                    "porcentaje_cierre": pd.to_numeric(row.iloc[5], errors="coerce"),
                    "duracion_cierre_min": pd.to_numeric(row.iloc[6], errors="coerce"),
                    "anotacion": row.iloc[8] if not pd.isna(row.iloc[8]) else None,
                    "culatas_pct": pd.to_numeric(row.iloc[17], errors="coerce"),
                }
            )

            registros.append(
                {
                    "fecha": fecha.date().isoformat(),
                    "bloque": bloque,
                    "lado": "B",
                    "elemento": row.iloc[15],
                    "hora_apertura": _limpiar_hora(row.iloc[9]),
                    "porcentaje_apertura": pd.to_numeric(row.iloc[10], errors="coerce"),
                    "duracion_apertura_min": pd.to_numeric(row.iloc[11], errors="coerce"),
                    "hora_cierre": _limpiar_hora(row.iloc[12]),
                    "porcentaje_cierre": pd.to_numeric(row.iloc[13], errors="coerce"),
                    "duracion_cierre_min": pd.to_numeric(row.iloc[14], errors="coerce"),
                    "anotacion": row.iloc[16] if not pd.isna(row.iloc[16]) else None,
                    "culatas_pct": pd.to_numeric(row.iloc[17], errors="coerce"),
                }
            )

    cortinas = pd.DataFrame(registros)
    cortinas = cortinas.dropna(subset=["elemento"], how="all")
    cortinas = cortinas.sort_values(["bloque", "fecha", "lado", "elemento"]).reset_index(drop=True)
    return cortinas


def limpiar_tabla_simple(hoja: str) -> pd.DataFrame:
    df = pd.read_excel(RAW_FILE, sheet_name=hoja)
    df.columns = [normalizar_columna(col) for col in df.columns]
    return df.drop_duplicates().reset_index(drop=True)


def limpiar_analisis_apertura() -> pd.DataFrame:
    df = pd.read_excel(RAW_FILE, sheet_name="Analisis Apertura", header=3)
    df.columns = [normalizar_columna(col) for col in df.columns]
    df = df.dropna(how="all")
    df = df.dropna(axis=1, how="all")
    df = df[[col for col in df.columns if not col.startswith("unnamed")]]
    if "bloque" in df.columns:
        df = df[df["bloque"].astype(str).str.contains("Bloque", na=False)]
    return df.reset_index(drop=True)


def exportar_csv(nombre: str, df: pd.DataFrame) -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    ruta = OUTPUT_DIR / nombre
    df.to_csv(ruta, index=False, encoding="utf-8-sig")
    print(f"{nombre}: {len(df):,} filas x {len(df.columns):,} columnas")


def main() -> None:
    if not RAW_FILE.exists():
        raise FileNotFoundError(f"No se encontro el archivo fuente: {RAW_FILE}")

    exportar_csv("wigga_limpio.csv", limpiar_wigga())
    exportar_csv("cortinas_limpio.csv", limpiar_cortinas())
    exportar_csv("ecowitt_limpio.csv", limpiar_tabla_simple("EcoWitt"))
    exportar_csv("apogee_limpio.csv", limpiar_tabla_simple("Apogge"))
    exportar_csv("analisis_apertura_limpio.csv", limpiar_analisis_apertura())


if __name__ == "__main__":
    main()
