# Sommer-Winter-Zeit
Interaktive Karten: https://nzzdev.github.io/visuals-sommer-winterzeit-analyse/

## Scripts
Diese Scripte generieren berechnen Sonnenaufgang und -Untergang für verschiedene Regionen und zu unterschiedlichen Zeiten.
* `0-create-baseshapes.ipynb`: Bereitet 2 Baseshapes vor: Einmal mit `nuts3` einmal mit einem `hexagonalen Grid`
* `1-calculate-times.ipynb`: Berechnet für jede Zelle die Sonnenaufgangs- und -untergangszeiten in Sommer- und Winterzeit. Erstellt ein Json
* `2-analyse.ipynb`: Generiert aus den Daten Karten

## Installation
VirtualEnv erstellen
```python
python3 -m venv env
```
VirtualEnv aktivieren
```python
source env/bin/activate
```
Requirements installieren
```python
pip install -r requirements.txt
```
Tippecanoe installieren
```bash
brew install tippecanoe
```

## Sources
* [NUTS3](https://ec.europa.eu/eurostat/web/gisco/geodata/statistical-units/territorial-units-statistics)
* [Coastlines](https://www.eea.europa.eu/data-and-maps/data/eea-coastline-for-analysis-2/gis-data/eea-coastline-polyline)
* [EuroGlobalMap](https://www.mapsforeurope.org/datasets/euro-global-map)
* [Countryborders](https://ec.europa.eu/eurostat/web/gisco/geodata/administrative-units/countries)