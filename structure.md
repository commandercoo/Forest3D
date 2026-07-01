# Forest3D — Project Structure

```
Forest3D/
│
├── configs/                          # Configuration files
│   ├── default.yaml                  # Default settings (baseline for all runs)
│   └── examples/                     # Ready-to-use presets
│       ├── coastal.yaml
│       ├── dense_forest.yaml
│       └── rocky_landscape.yaml
│
├── dem/                              # Digital Elevation Model input data
│   ├── terrain.tif                   # Raw DEM raster
│   ├── terrain_enhanced.tif          # Pre-processed DEM
│   ├── enhanced_heightmap.tif        # Heightmap derived from DEM
│   └── demgazebo.dem                 # Gazebo-ready DEM format
│
├── Blender-Assets/                   # Drop Blender models here before converting
│   ├── tree/
│   ├── bush/
│   ├── grass/
│   ├── rock/
│   └── soil/
│
└── docker/                           # Container-based setup (optional)
    ├── Dockerfile
    ├── Dockerfile.dev
    └── docker-compose.yml
```

## CLI Commands

After installing (`pip install .`), the `forest3d` command is available:

| Command | Description |
|---|---|
| `forest3d terrain --dem <file.tif>` | Process a DEM file into Gazebo terrain |
| `forest3d convert --input ./Blender-Assets --output ./models` | Convert Blender assets to Gazebo models |
| `forest3d generate --density '{"tree": 50, "rock": 10}'` | Populate the world with vegetation/objects |
| `forest3d launch` | Launch the generated world in Gazebo |

Pass `-c <config.yaml>` to any command to use a custom configuration file.

## Environment Variables

| Variable | Purpose |
|---|---|
| `FOREST3D_BLENDER_PATH` | Path to the Blender executable |
| `FOREST3D_BASE_PATH` | Project base directory |
| `FOREST3D_MODELS_PATH` | Output directory for converted models |
