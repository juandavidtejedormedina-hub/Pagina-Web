# Preparacion para analisis estadistico

Esta etapa usa los archivos de `Datos/Analiticos/` y genera reportes base en
`Datos/Reportes/`.

Comando:

```powershell
.\.venv\Scripts\python.exe procesamiento\preparar_analisis_estadistico.py
```

Reportes generados:

| Reporte | Descripcion |
| --- | --- |
| `preparacion_analisis_estadistico.csv` | Filas, columnas, nulos, duplicados y rango temporal por dataset. |
| `estadistica_descriptiva_numerica.csv` | Media, mediana, desviacion, minimos, maximos y cuartiles. |
| `estadistica_descriptiva_categorica.csv` | Valores unicos, nulos y valor mas frecuente. |
| `posibles_outliers_iqr.csv` | Posibles outliers por IQR para variables continuas. |

El reporte de outliers no elimina datos. Solo marca valores para revisar en
graficas o analisis posterior. Se excluyen variables binarias, variables con
muy pocos valores unicos y datasets demasiado pequenos, porque ahi el metodo
IQR puede generar senales poco utiles.

Estado actual:

| Dataset | Estado |
| --- | --- |
| WIGGA | Listo para estadistica |
| Cortinas | Listo para estadistica |
| EcoWitt | Listo para estadistica |
| Apogee | Listo para estadistica |
| Analisis Apertura | Listo para estadistica |
| Analisis Apertura Areas | Listo para estadistica |
