# Sommer-Winter-Zeit
Dieses Repo enthält alle Scripte und Daten, die wir zur Berechnung [dieses Artikels](https://www.nzz.ch/-ld.1877525) verwendet haben.

## Testkarten
Interaktive Karten: https://nzzdev.github.io/visuals-sommer-winterzeit-analyse/

## Installation
Requirements installieren
```python
pip install -r requirements.txt
```
Tippecanoe installieren
```bash
brew install tippecanoe
```

## Scripts
### `0-create-baseshapes.ipynb`
* Generiert ein Hexgrid in der Grösse von Europa mit Durchmesser von 50km
* Speichert die Zeitzone für jede Zelle
* Lädt von OSM alle Ortschaften herunter
* Benennt jede Zelle anhand der grössten Ortschaft

Outputs: 
* `export/hexagons.gpkg`
* `export/citylabels.gpkg`

### `1-calculate-times.ipynb`
Hier geschehen alle Berechnungen der Sonnenzeiten.

Teil 1: Time of Sunrise/Sunset:
* Für jedes Hexagon wird für jeden Tag im Jahr der Sonnenauf- und Untergang für 3 Szenarien berechnet berechnet.
  * Aktuelles System
  * Immer Sommerzeit
  * Immer Winterzeit
* Der frühste Sonnenauf- und Untergang sowie der späteste Sonnenauf- und Untergang für jedes Szenario werden mit der ID des Hexagons gespeichert

Teil 2: Calculate amount of light at certain hours
* Dies wird für die Einfärbung der Karte gebraucht
* Für jedes Szenario von oben wird für jede Stunde an jedem Tag die Sonnenposition berechnet.

Outputs:
* `export/timedata-hex.json`
* `export/timedata-hourly-hex.json`

Alle Daten werden als JSON mit Referenz auf die Hexagon-Zelle und die Zeitzone gespeichert. Format des JSON:
```json
[
  {
    "nuts_id": 0,
    "timezone": "Europe/Zagreb",
    "sunrise": {
      "summer": {
        "earliest": "04:57:24.597567",
        "earliest_day": "2025-06-15",
        "latest": "08:23:57.174537",
        "latest_day": "2025-01-02"
      },
      "winter": {
        "earliest": "03:57:24.597567",
        "earliest_day": "2025-06-15",
        "latest": "07:23:57.174537",
        "latest_day": "2025-01-02"
      },
      "current": {
        "earliest": "04:57:24.597567",
        "earliest_day": "2025-06-15",
        "latest": "07:23:57.174537",
        "latest_day": "2025-01-02"
      }
    }
  }
]
```

### `2-analyze.ipynb`
Analysiert die Daten und generiert [interaktive Karten](https://nzzdev.github.io/visuals-sommer-winterzeit-analyse/), die automatisiert auf GitHub-Pages hochgeladen werden. Die Scripte funktionieren vermutlich nicht mehr, da das Datenmodell geändert hat.

### `3-web-export-grid.ipynb`
Generiert anhand den errechneten Daten (`timedata-hex.json`) sowie des Hexgrid (`hexagon.geojson`) die entsprechenden GeoJSONs.
Output:
* `export/web/popupdata.geojson`

### `4-web-export-hourly.ipynb`
Generiert anhand den errechneten Stundenwerten (`timedata-hourly-hex.json`) sowie des Hexgrid (`hexagon.geojson`) die entsprechenden GeoJSONs.
Output:
* `export/web/sunrise-earliest-summer.geojson`
* `export/web/sunrise-earliest-winter.geojson`
* `export/web/sunrise-latest-summer.geojson`
* `export/web/sunrise-latest-winter.geojson`
* `export/web/sunset-earliest-summer.geojson`
* `export/web/sunset-earliest-winter.geojson`
* `export/web/sunset-latest-summer.geojson`
* `export/web/sunset-latest-winter.geojson`

### `5-web-export-timezones.ipynb`
Generiert GeoJSONs für:
* Zeitzonen gemäss 15°-Linie
* Gemäss Ländergrenzen

Diese Daten wurden nicht verwendet

### `6-web-export-create-mbtile.ipynb`
Verschmelzt alle GeoJSONS zu einem mbtile zur Weiterverwendung in einem Kartenclouddienst wie Maptiler oder Mapbox.

### `99-bubble-chart.ipynb`
Generiert Daten für DataWrapper-Charts

### `99-tests.ipynb`
Helfer, um die Daten mit Stichproben zu prüfen
