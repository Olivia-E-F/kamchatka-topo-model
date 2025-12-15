import os
import subprocess

# ==================================
# DEM Reprojection:
#   Reproject each raw DEM tile from
#   EPSG:4326 to EPSG:32657 (UTM 57N)
# ==================================

# ----------------------------------
# Config
# ----------------------------------

RAW_DEM_DIR = "data/raw"
OUTPUT_DIR = "data/processed/utm_tiles"

TARGET_CRS = "EPSG:32657"
NODATA_VALUE = -9999

# ----------------------------------
# DEM Reprojection
# ----------------------------------

def reproject_tiles():
    """
    Reproject each DEM such that elevation 
    values are preserved; only spatial
    reference is altered.
    """

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    dem_tiles = [
        f for f in os.listdir(RAW_DEM_DIR)
        if f.lower().endswith(".tif")
    ]

    if not dem_tiles:
        raise RuntimeError("No DEM tiles found in data/raw")
    
    for fname in dem_tiles:
        input_path = os.path.join(RAW_DEM_DIR, fname)
        output_path = os.path.join(
            OUTPUT_DIR,
            fname.replace(".tif", "_utm57.tif")
        )
        
        cmd = [
            "gdalwarp",
            "-t_srs", TARGET_CRS,
            "-r", "bilinear",
            "-tr", "30", "30",
            "-tap",
            "-dstnodata", str(NODATA_VALUE),
            "-of", "GTiff",
            input_path,
            output_path
        ]
        
        subprocess.run(cmd, check = True)

# ----------------------------------
# Entry
# ----------------------------------

if __name__ == "__main__":
    reproject_tiles()