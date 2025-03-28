from pathlib import Path

PATH_NUTS_EU = Path('../data/nuts3/NUTS_RG_20M_2024_4326.geojson')
PATH_NUTS_UK = Path('../data/nuts3/NUTS_Level_3_January_2018_GCB_in_the_United_Kingdom_2022_-764267078201060548.geojson')
PATH_BOUNDARIES = Path('../data/europeboundaries.geojson')
PATH_HEXAGON = Path('../export/hexagons.gpkg')
PATH_MASTERNUTS = Path('../export/masternuts.gpkg')
PATH_TIMEDATA_NUTS = Path('../export/timedata-nuts.json')
PATH_TIMEDATA_HEX = Path('../export/timedata-hex.json')
PATH_TIMEDATA_HOURLY_HEX = Path('../export/timedata-hourly-hex.json')
PATH_DOCS = Path('../docs')
PATH_BORDERS = Path('../data/CNTR_RG_20M_2024_4326.geojson')
PATH_GEOJSON_EXPORT = Path('../export/web/grid.geojson')
PATH_MBTILE_EXPORT = Path('../export/web/grid.mbtiles')
PATH_MBTILE_COMBINED  = Path('../export/web/zeitumstellung.mbtiles')
PATH_WEBEXPORT = Path('../export/web/')
PATH_HEXAGRID_TIMEDATA = Path('../export/hexagons-timedata.gpkg')
PATH_GEOJSON_HOURLY = PATH_WEBEXPORT / 'grid-hourly.geojson'
PATH_GEOJSON_TIMEZONES = PATH_WEBEXPORT / 'timezone-lines.geojson'
PATH_MBTILES_TIMEZONES = PATH_WEBEXPORT / 'timezone-lines.mbtiles'
PATH_GEOJSON_COUNTRIES = PATH_WEBEXPORT / 'countries.geojson'
PATH_MBTILES_COUNTRIES = PATH_WEBEXPORT / 'countries.mbtiles'
PATH_GEOJSON_POPUPDATA = Path('../export/web/popupdata.geojson')

REMOVE_TIMEZONES = ['Africa/Ceuta', 'Africa/Casablanca', 'Europe/Moscow', 'Europe/Belarus', 'Europe/Minsk', 'Europe/Kyiv', 'Europe/Kaliningrad', 'Europe/Istanbul']