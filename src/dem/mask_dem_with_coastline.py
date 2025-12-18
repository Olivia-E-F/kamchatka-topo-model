import subprocess
from pathlib import Path 

# ========================================
# Mask DEM with Coastline
# Uses coastline polygon to remove ocean and crop dem to land
# I.E: What pixels are LAND pixels
# ========================================

PROJECT_ROOT = Path(__file__).resolve().parents[2]

DEM_PATH = (
    PROJECT_ROOT / "data" / "raster" / "merged"
    / "kamchatka_dem_merged_laea.tif"
)

COASTLINE_PATH = (
    PROJECT_ROOT / "data" / "vector"
    / "kamchatka_coastline.geojson"
)

OUTPUT_DIR = (
    PROJECT_ROOT / "data" / "raster" / "masked"
)

OUTPUT_DEM = OUTPUT_DIR / "kamchatka_dem_laea_land_only.tif"

NODATA_VALUE = -9999

# --------------------------------------
# Mask Function
# --------------------------------------

def mask_dem_with_coastline():
    print("Project Root:")
    print(PROJECT_ROOT)

    print("\nInput DEM:")
    print(DEM_PATH)

    print("\nCoastline Vector:")
    print(COASTLINE_PATH)

    if not DEM_PATH.exists():
        raise RuntimeError(f"DEM not found: {DEM_PATH}")

    if not COASTLINE_PATH.exists():
        raise RuntimeError(f"Coastline not found: {COASTLINE_PATH}")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    cmd = [
        "gdalwarp",
        "-cutline", str(COASTLINE_PATH),
        "-crop_to_cutline",
        "-dstnodata", str(NODATA_VALUE),
        "-of", "GTiff",
        str(DEM_PATH),
        str(OUTPUT_DEM),
    ]

    print("\nRunning Command:")
    print(" ".join(cmd))

    subprocess.run(cmd, check=True)

    print("\nMasked DEM written to:")
    print(OUTPUT_DEM)

# --------------------------------------
# Entry Point
# --------------------------------------

if __name__ == "__main__":
    mask_dem_with_coastline()
