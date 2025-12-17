import os
import subprocess

# ================================
# Mask DEM with Coastline
# Uses coastline polygon to remove ocean and crop dem to land

DEM_PATH = "data/raster/merged/kamchatka_dem_utm57.tif"
COASTLINE_PATH = "data/vector/kamchatka_coastline.geojson"
OUTPUT_PATH = "data/raster/masked/kamchatka_dem_land_utm57.tif"
