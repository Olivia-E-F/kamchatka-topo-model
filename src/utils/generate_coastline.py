import geopandas as gpd
from shapely.geometry import Polygon
import shapely
import os

## Config ##

# Path to OSM land Polygons
OSM_LAND_PATH = "data/osm/land-polygons-complete-4326/land_polygons.shp"

# Rough region of interest (as defined in research) polygon
ROI_PATH = "data/rough_roi.geojson"

OUTPUT_PATH = "data/kamchatka_coastline.geojson"

# Simplification tolerance (deg.) for med.-res. ouput (R2)
# ~0.01 degrees ~ 1km
SIMPLIFY_TOLERANCE = 0.01 # ** Alter for Later

## Loading Data 

print("Loading OSM Coastline Polygons :) :) :)")
land = gdp.read_file(OSM_LAND_PATH)

print("Loading rough ROI polygon :) :) :)")
roi = gdp.read_file(ROI_PATH)

# Ensuring both layers use the same CRS (WGS84)
land = land.to_crs("EPSG:4326")
roi = roi.to_crs("ESPG:4326")


## Clip Coastline with ROI

print("Clipping land polygons to ROI :) :) :)")
clipped = gpd.overlay(land, roi, how="intersection") # **

# Clipping could yield multiple features, dissolve into a single geometry. 
print("Dissolving clipped polygons :) :) :)")
clipped = clipped.dissolve()

## Optimal Geometry Simplification

print("simplifying coastline :) :) :)")
clipped["geometry"] = clipped["geometry"].simplify(
    SIMPLIFY_TOLERANCE, preserve_topology = True
)

# Fix Geometry if needed

# Shapely buffer(0) is a classic fix for invalid geometrics
print("Validating geometry :) :) :)")

clipped["geometry"] = clipped["geometry"].buffer(0)

# Save Output

print(f"Saving final coastline to {OUTPUT_PATH} :) :) :)")
clipped.to_file(OUTPUT_PATH, driver="GeoJSON")

print("Done  :) Coastline Exported!")

