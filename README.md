# Kamchatka Peninsula 3D Topographic Model

This project generates a high-resolution, four-tile 3D-printable topographic model of the **Kamchatka Peninsula** using the **12.5 m ALOS PALSAR DEM** dataset.  
All processing is performed in Python through a modular geospatial and mesh-generation pipeline.

The final outputs include:

- Four STL terrain tiles arranged in a 2×2 grid  
- Four PNG heightmaps for painting reference  
- 1.5× vertical exaggeration  
- 5 mm recessed ocean surface  
- 4 mm flat base  
- Round 6 mm alignment pins and sockets  

## Motivation 

Believe it or not, this volcano-ridden tundra is my birthplace. It’s a fun fact that always surprises people, and it inspired me to take on a project that blends geospatial data, Python, and 3D printing to recreate this terrain in high resolution. Once the model is printed, I plan to hand-paint it to add visual depth, highlight elevation features, and bring the landscape to life.

## Tile Layout (2×2 Grid)
[ tile_1 (NW) | tile_2 (NE) ]
[ tile_3 (SW) | tile_4 (SE) ]

Each tile is sized to fit within the build volume of printers such as the Prusa MK4 and includes:

- 4 mm base  
- 5 mm ocean recession  
- 1.5× vertical exaggeration  
- 6 mm round alignment pins  

## Environment Setup

Create and activate the conda environment:

```bash
conda env create -f environment.yml
conda activate kamchatka
```