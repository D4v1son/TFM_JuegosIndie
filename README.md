# Auge del Indie: análisis predictivo y visualización del mercado de videojuegos independientes

Repositorio del Trabajo Fin de Estudios del Máster Universitario en Análisis y Visualización de Datos Masivos (UNIR).

- **Autor:** David Vicente Moya
- **Director:** Diego Fernández García

## ¿De qué trata?

El trabajo estudia qué factores se asocian al éxito comercial de un videojuego independiente (*indie*) en Steam y cómo ha evolucionado su cuota de mercado frente a los grandes títulos (AAA). Para ello se combinan:

1. Un **análisis exploratorio** de datos históricos de Steam.
2. Un **modelo predictivo** del éxito comercial.
3. Un **dashboard interactivo** para explorar el mercado.

## Estado del proyecto

| Parte | Estado |
|---|---|
| Análisis exploratorio del dataset de Kaggle | Hecho |
| Contraste de propietarios con una muestra de SteamSpy | Pendiente |
| Modelo predictivo | Pendiente |
| Dashboard interactivo | Pendiente |

## Estructura del repositorio

```
notebooks/   Cuadernos de análisis (kaggle_eda.ipynb)
src/         Scripts auxiliares
figuras/     Figuras generadas por los cuadernos
data/        Datos locales (no se incluyen en el repositorio)
```

## Datos

Los datos no se incluyen por su tamaño. Hay que descargarlos y colocarlos así:

1. Descargar el [Steam Games Dataset](https://www.kaggle.com/datasets/fronkongames/steam-games-dataset) (autor: FronkonGames, licencia MIT).
2. Guardar `games.csv` en `data/kaggle/steam_games_dataset/`.

La versión usada en el trabajo se descargó el 10-11-2026 (última actualización en Kaggle: 08-11-2026). Según su ficha, los datos proceden de Steam. Contienen estimaciones de propietarios por rangos, no ventas reales.

## Cómo reproducir el análisis

1. Crear el entorno (Python 3.11):
   ```
   conda env create -f environment.yml
   conda activate tfm_indie
   ```
2. Colocar los datos como se indica arriba.
3. Abrir `notebooks/kaggle_eda.ipynb` y ejecutar todas las celdas. Las figuras se guardan en `figuras/`.

## Decisiones principales del análisis

- **Definición de indie:** presencia del género *Indie* (`Genres`); la etiqueta (`Tags`) se usa como análisis de sensibilidad.
- **Periodo descriptivo:** 2010-2025 (2026 está incompleto).
- **Modelado:** solo con juegos publicados al menos 12 meses antes de la descarga, para evitar sesgos por falta de madurez.

## Licencia

- **Código:** [elegir, por ejemplo MIT].
- **Datos:** los del conjunto de Kaggle se rigen por su licencia (MIT); no se redistribuyen aquí.

## Cita

Vicente Moya, D. (2026). *Auge del Indie: análisis predictivo y visualización del mercado de videojuegos independientes* [Software]. GitHub. https://github.com/D4v1son/TFM_JuegosIndie