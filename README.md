# Tree Cover England

This project analyses tree cover and income deprivation data for Lower Layer Super Output Areas (LSOAs) in England.

## Data Sources

-   [LSOAs England and Wales](https://geoportal.statistics.gov.uk/datasets/02e8d336d6804fbeabe6c972e5a27b16/explore?location=51.611648%2C-2.291229%2C8.59) - Converted to WGS84
-   [Tree cover data](https://policy.friendsoftheearth.uk/insight/mapping-english-tree-cover-results-ranking-and-methodology)
-   [Buildings data](https://osdatahub.os.uk/downloads/open/OpenMapLocal) - Converted to WGS84

## Data Processing

The data processing is done using Python scripts located in the `scripts` directory:

1. `merge.py`: Merges the tree cover and income deprivation data based on LSOA codes.
2. `process.py`: Combines the merged data with the LSOAs GeoJSON file, updating the GeoJSON features with tree cover and income rank properties.
3. `intersect.py`: Filters the updated LSOAs GeoJSON file and intersects it with the buildings data to create a new GeoJSON file with intersected buildings.

## Commands

The following commands are used to generate vector tiles from the GeoJSON files:

Splits the large buildings file

```bash
    python scripts/split.py
```

Simplifies the large buildings files

```bash
    node --max-old-space-size=32000 /usr/local/bin/mapshaper -i output/split/part01.geojson -simplify 10% keep-shapes -o output/split/simplified_part01.geojson
    node --max-old-space-size=32000 /usr/local/bin/mapshaper -i output/split/part02.geojson -simplify 10% keep-shapes -o output/split/simplified_part02.geojson
    node --max-old-space-size=32000 /usr/local/bin/mapshaper -i output/split/part03.geojson -simplify 10% keep-shapes -o output/split/simplified_part03.geojson
    node --max-old-space-size=32000 /usr/local/bin/mapshaper -i output/split/part04.geojson -simplify 10% keep-shapes -o output/split/simplified_part04.geojson
    node --max-old-space-size=32000 /usr/local/bin/mapshaper -i output/split/part05.geojson -simplify 10% keep-shapes -o output/split/simplified_part05.geojson
    node --max-old-space-size=32000 /usr/local/bin/mapshaper -i output/split/part06.geojson -simplify 10% keep-shapes -o output/split/simplified_part06.geojson
    node --max-old-space-size=32000 /usr/local/bin/mapshaper -i output/split/part07.geojson -simplify 10% keep-shapes -o output/split/simplified_part07.geojson
```

Combines the large building files

```bash
    python scripts/combine.py
```

```bash
    tippecanoe --output=output/filtered-LSOA.pmtiles --generate-ids --force --no-feature-limit --no-tile-size-limit --detect-shared-borders --coalesce-fraction-as-needed --coalesce-densest-as-needed --coalesce-smallest-as-needed --coalesce --reorder --minimum-zoom=0 --maximum-zoom=15 -r1 output/filtered_LSOA.geojson
```

```bash
    tippecanoe --output=output/simplified-buildings.pmtiles --generate-ids --force --no-feature-limit --no-tile-size-limit --detect-shared-borders --coalesce-fraction-as-needed --coalesce-densest-as-needed --coalesce-smallest-as-needed --coalesce --reorder --minimum-zoom=0 --maximum-zoom=15 -r1 output/simplified_buildings.geojson
```
