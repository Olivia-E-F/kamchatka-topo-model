# OpenStreetMap Land Polygons (Not Tracked)

This directory contains large OpenStreetMap-derived land polygon shapefiles
used to extract coastlines for the Kamchatka peninsula.

These files are intentionally excluded from version control due to size
and are expected to be downloaded locally by the user.

## Data source
- https://osmdata.openstreetmap.de/data/land-polygons.html
- Dataset: WGS84 / EPSG:4326

## Expected directory structure

After downloading and extracting the dataset, place it here:

data/osm/land-polygons-complete-4326/
├── land_polygons.shp
├── land_polygons.shx
├── land_polygons.dbf
├── land_polygons.prj
└── README.txt

## Notes
- This data is used only as an intermediate source for coastline extraction
- Derived, clipped outputs may be committed if kept reasonably small
