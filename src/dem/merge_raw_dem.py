import subprocess
from pathlib import Path

# ======================================
# Merge Raw Cop. DEM tiles (EPSG:4326)
# ======================================

# --------------------------------------
# Resolve Project Root
# --------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[2]
RAW_DEM_DIR = PROJECT_ROOT / "data" / "source" / "dem"
OUTPUT_DIR = PROJECT_ROOT / "data" / "raster" / "merged"
OUTPUT_DEM = OUTPUT_DIR / "kamchatka_dem_merged_raw.tif"


# --------------------------------------
# Merge Func
# --------------------------------------

def merge_raw_dem():
    # having path issues, leaving this in for continuity
    print(f"Project Root: {PROJECT_ROOT}")
    print(f"Looking for DEM tiles in: {RAW_DEM_DIR}")
    
    if not RAW_DEM_DIR.exists():
        raise RuntimeError(f"RAW_DEM_DIR does not exist: {RAW_DEM_DIR}")
    
    dem_tiles = sorted(RAW_DEM_DIR.glob("*.tif"))

    print(f"Found {len(dem_tiles)} DEM tiles")
    for t in dem_tiles:
        print(f" - {t.name}")

    if not dem_tiles:
        raise RuntimeError("No DEM tiles found to merge")
    
    print("Inspecting first DEM Tile with gdalinfo")
    subprocess.run(
        ["gdalinfo", str(dem_tiles[0])],
        check = True
    )

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    cmd = [
        "gdal_merge.py",
        "-o", str(OUTPUT_DEM),
        "-of", "GTiff",
        *map(str, dem_tiles),
    ]

    print("Running Command:")
    print(" ".join(cmd))

    subprocess.run(cmd, check=True)

    print(f"Merged DEM written to: {OUTPUT_DEM}")

# --------------------------------------
# Entry
# --------------------------------------

if __name__ == "__main__":
    merge_raw_dem()