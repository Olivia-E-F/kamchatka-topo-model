import os
import subprocess
from src.config import SOURCE_CRS, KAMCHATKA_LAEA_PROJ

# ==================================
# DEM Reprojection:
#   Reproject each raw DEM tile into
#   Kamchatka Regional LAEA Project.
# ==================================

# ----------------------------------
# Config
# ----------------------------------

RAW_DEM_DIR = "data/source/dem"
OUTPUT_DIR = "data/raster/reprojected_tiles"

# ----------------------------------
# Projection Parameters
# ----------------------------------

RESOLUTION_METERS = 30  # Target Ground Resolution
NODATA_VALUE = -9999

# ----------------------------------
# Test Config
# ----------------------------------
# enter file name [] to test specific file
# leave empty list [] to reproject ALL les

TEST_TILES = [
#    "output_hh_2.tif" # the middle tile's giving me GREIF.
]

# ----------------------------------
# DEM Reprojection
# ----------------------------------

def reproject_tiles(test_single_file = True):
    """
    Reproject DEM tiles from EPSG:4326 into
    a regional LAEA projection centered on Kamchatka.

    If test_single_tile=True, only reprojects the
    first tile found (for visual validation).
    """

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    if TEST_TILES:
        dem_tiles = TEST_TILES
        print(f"TEST MODE: Reprojecting {dem_tiles}")
    else:
        dem_tiles = sorted([
            f for f in os.listdir(RAW_DEM_DIR)
            if f.lower().endswith(".tif")
        ])
        print("FULL MODE: Reprojecting ALL tiles.")
    
    if not dem_tiles:
        raise RuntimeError("No Dem Tiles selected for reprojeciton")
    
    for fname in dem_tiles:
        input_path = os.path.join(RAW_DEM_DIR, fname)

        if not os.path.exists(input_path):
            raise FileNotFoundError(f"Missing DEM Tile: {input_path}")
        
        output_path = os.path.join(
            OUTPUT_DIR,
            fname.replace(".tif", "_laea.tif")
        )
        
        cmd = [
            "gdalwarp",
            "-overwrite",
            "-s_srs", SOURCE_CRS,
            "-t_srs", KAMCHATKA_LAEA_PROJ,
            "-tr", str(RESOLUTION_METERS), str(RESOLUTION_METERS),
            "-r", "bilinear",
            "-dstnodata", str(NODATA_VALUE),
            "-of", "GTiff",
            input_path,
            output_path
        ]
        
        subprocess.run(cmd, check = True)
        print(f"Created: {output_path}")

# ----------------------------------
# Entry
# ----------------------------------

if __name__ == "__main__":
    reproject_tiles()