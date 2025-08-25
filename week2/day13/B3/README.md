# UrbanMove – Paradas de Autobús en Santander

Este proyecto forma parte del Bootcamp personal de análisis y visualización de datos.  
El objetivo es construir un **pipeline reproducible** que integre datos abiertos en un dashboard interactivo de Power BI.

---

## 🚍 Descripción del proyecto
UrbanMove es una empresa ficticia de transporte urbano utilizada como caso de estudio.  
A partir de la **API de datos abiertos del Ayuntamiento de Santander**, se ha creado un flujo completo:

1. **Extracción de datos** desde la API oficial.  
2. **Limpieza y normalización** en Python con Pandas.  
3. **Exportación** a ficheros CSV (dataset limpio y dataset completo).  
4. **Visualización** en Power BI con un dashboard interactivo.  

---

## 📂 Estructura de carpetas

### B1 — Extracción y limpieza (Python)
- `tus_api.py` → Script en Python para conectarse a la API, limpiar datos y generar CSV.  
- `paradas_tus.csv` → Dataset limpio, listo para Power BI.  
- `paradas_tus_full.csv` → Respaldo completo con todos los campos originales de la API.  

### B2 — Visualización (Power BI)
- `urbanmove_PBI_proyect.pbix` → Archivo de Power BI con el dashboard final.  
- `urbanmove_PBI_Dashboard.png` → Imagen exportada del dashboard.  

### B3 — Documentación
- `README.md` (este archivo).  

---

## 📊 Dashboard final

El dashboard incluye:  
- **KPIs principales**:  
  - Total de paradas  
  - Total de sentidos  
  - Promedio de paradas por sentido  
- **Mapa interactivo** con coordenadas (latitud/longitud) de cada parada.  
- **Segmentador por sentido** para explorar rutas específicas.  
- **Top 10 sentidos con más paradas** en gráfico de barras.  

![UrbanMove Dashboard](../B2/urbanmove_PBI_Dashboard.png)

---

## 🔗 Fuente de datos
- [Datos abiertos Santander – Paradas de bus](https://datos.santander.es/api/datos/paradas_bus.json)  

---

## 📌 Reproducibilidad
1. Clonar este repositorio.  
2. Ir a la carpeta `B1` y ejecutar el script:  
   ```bash
   python3 tus_api.py
