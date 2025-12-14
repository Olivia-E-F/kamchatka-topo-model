import geopandas as gpd
from shapely.geometry import Polygon
import shapely
import os

# --------------------------------------------------
# Config
# --------------------------------------------------

# Global OSM land polygons (authoritative land / ocean boundary)
OSM_LAND_PATH = "data/osm/land-polygons-complete-4326/land_polygons.shp"

# Rough region-of-interest polygon defining Kamchatka + Koryak extent
# Used only as a spatial cutter, not as a final boundary
ROI_PATH = "data/rough_roi.geojson"

# Output coastline polygon for downstream DEM masking and STL generation
OUTPUT_PATH = "data/kamchatka_coastline.geojson"

# Geometry simplification tolerance (meters)
# Chosen to remove sub-print-scale coastline noise while preserving major features
SIMPLIFY_TOLERANCE = 500


# --------------------------------------------------
# Load source geometries
# --------------------------------------------------

land = gpd.read_file(OSM_LAND_PATH)
roi  = gpd.read_file(ROI_PATH)


# --------------------------------------------------
# Topological alignment phase
# Purpose: ensure valid geometric operations (not distance measurement)
# --------------------------------------------------

# Reproject both layers into a common geographic CRS so polygon intersection is valid
land = land.to_crs("EPSG:4326")
roi  = roi.to_crs("EPSG:4326")


# --------------------------------------------------
# Coastline extraction
# Purpose: physically cut global land polygons to the Kamchatka region
# --------------------------------------------------

# Use polygon intersection (not bounding box or spatial filtering)
# This trims land geometry exactly to the ROI boundary and preserves coastline shape
clipped = gpd.overlay(land, roi, how="intersection")

# Intersection yields many fragmented features; dissolve into a single landmass polygon
clipped = clipped.dissolve()


# --------------------------------------------------
# Metric processing phase
# Purpose: distance-aware simplification and raster compatibility
# --------------------------------------------------

# Reproject into a metric CRS so simplification tolerance corresponds to real distances
# UTM Zone 57N is appropriate for Kamchatka
clipped = clipped.to_crs("EPSG:32657")

# Simplify coastline geometry while preserving topological validity
clipped["geometry"] = clipped["geometry"].simplify(
    SIMPLIFY_TOLERANCE,
    preserve_topology=True
)

# Repair any minor invalid geometry introduced by simplification
clipped["geometry"] = clipped["geometry"].buffer(0)


# --------------------------------------------------
# Export
# --------------------------------------------------

clipped.to_file(OUTPUT_PATH, driver="GeoJSON")
print(f"Exported coastline to {OUTPUT_PATH}")
