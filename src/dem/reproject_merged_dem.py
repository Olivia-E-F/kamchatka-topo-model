import subprocess
from pathlib import Path

# ======================================
# Reproject merged Kamchatka DEM to LAEA
# ======================================

PROJECT_ROOT = Path(__file__).resolve().parents[2]

INPUT_DEM = (PROJECT_ROOT / "data" / "raster" / "merged" / "kamchatka_dem_merged_raw.tif")
OUTPUT_DEM = (PROJECT_ROOT / "data" / "raster" / "merged" / "kamchatka_dem_merged_laea.tif")

LAEA_PROJ = (
    "+proj=laea "
    "+lat_0=56 "
    "+lon_0=160 "
    "+datum=WGS84 "
    "+units=m "
    "+no_defs"
)

# --------------------------------------
# Reproject Func
# --------------------------------------

def reproject_merged_dem():
    print(f"Project Root: {PROJECT_ROOT}")
    print(f"Input DEM: {INPUT_DEM}")

    if not INPUT_DEM.exists():
        raise RuntimeError(f"Input DEM doesn't exist: {INPUT_DEM}")
    
    print("Insepcting input DEM:")
    subprocess.run(
        ["gdalinfo", str(INPUT_DEM)],
        check=True
    )

    OUTPUT_DEM.parent.mkdir(parents=True, exist_ok=True)

    cmd = [
        "gdalwarp",
        "-t_srs", LAEA_PROJ,
        "-r", "bilinear",
        "-dstnodata", "-9999",
        str(INPUT_DEM),
        str(OUTPUT_DEM),
    ]

    print("Running CMD:")
    print(" ".join(cmd))

    subprocess.run(cmd, check=True)

    print (f"Reprojected DEM Written to: {OUTPUT_DEM}")

    print("Inspecting Ouput DEM:")
    subprocess.run(
        ["gdalinfo", str(OUTPUT_DEM)],
         check=True
    )
# --------------------------------------
# Entry
# --------------------------------------

if __name__ == "__main__":
    reproject_merged_dem()
    