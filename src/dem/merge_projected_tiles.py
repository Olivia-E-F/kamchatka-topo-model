import os
import subprocess

# ===========================
# Merge projected DEM Tiles
#
# Merges UTM-projected tiles 
# into a single dem
# ==========================

PROJECTED_TILE_DIR = "data/raster/utm_tiles"
OUTPUT_DEM_PATH = "data/raster/merged/kamchatka_dem_utm57.tif"

def merge_projected_tiles():
    tiles = sorted([
        os.path.join(PROJECTED_TILE_DIR, f)
        for f in os.listdir(PROJECTED_TILE_DIR)
        if f.lower().endswith(".tif")
    ])

    if len(tiles) < 2:
        raise RuntimeError(
            f"Expected at least two projected tiles, found {len(tiles)}."
        )
    
    os.makedirs(os.path.dirname(OUTPUT_DEM_PATH), exist_ok=True)

    cmd = [
        "gdal_merge.py",
        "-o", OUTPUT_DEM_PATH,
        "-of", "GTiff",
        *tiles
    ]

    subprocess.run(cmd, check=True)

if __name__ == "__main__":
    merge_projected_tiles()