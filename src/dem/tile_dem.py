import os
import subprocess
from pathlib import Path

# ======================================
# Tile Masked LAEA DEM into printable chunks
# ======================================

# --------------------------------------
# Paths
# --------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[2]

INPUT_DEM_PATH = PROJECT_ROOT / "data" / "raster" / "masked" / "kamchatka_dem_laea_land_only.tif"
OUTPUT_TILE_DIR = PROJECT_ROOT / "data" / "raster" / "tiles"

# Tile size in pixels
# ** (adjust later based on printer size)
TILE_WIDTH_PX = 13000
TILE_HEIGHT_PX = 24000


# --------------------------------------
# Tile function
# --------------------------------------

def tile_dem():
    print(f"Input DEM: {INPUT_DEM_PATH}")

    if not INPUT_DEM_PATH.exists():
        raise RuntimeError(f"Input DEM does not exist: {INPUT_DEM_PATH}")

    OUTPUT_TILE_DIR.mkdir(parents=True, exist_ok=True)

    cmd = [
        "gdal_retile.py",
        "-ps", str(TILE_WIDTH_PX), str(TILE_HEIGHT_PX),
        "-targetDir", str(OUTPUT_TILE_DIR),
        "-of", "GTiff",
        "-co", "COMPRESS=LZW",
        str(INPUT_DEM_PATH),
    ]

    print("Running command:")
    print(" ".join(cmd))

    subprocess.run(cmd, check=True)

    print(f"Tiling complete. Tiles written to: {OUTPUT_TILE_DIR}")


# --------------------------------------
# Entry point
# --------------------------------------

if __name__ == "__main__":
    tile_dem()
