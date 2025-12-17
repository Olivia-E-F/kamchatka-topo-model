# ===========================
# Projection Source of Truth
# ===========================

# Source DEM CRS( Cop. GLO-30)
SOURCE_CRS = "EPSG:4326"

# Regional Projection for Kamchatka
# Lambert Azimuthal Equal Area
#   Centered on Central Kmchtk.

KAMCHATKA_LAEA_PROJ = (
    "+proj=laea "
    "+lat_0 = 56 "
    "+lon_0 = 160 "
    "+x_0 = 0 "
    "+y_0 = 0 "
    "datum = WGS84 "
    "+units = m "
    "+no_defs"
)
