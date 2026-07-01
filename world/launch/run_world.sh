#!/usr/bin/env bash
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
WORLD_DIR="$(dirname "$SCRIPT_DIR")"

export GAZEBO_MODEL_PATH="$WORLD_DIR/models:$GAZEBO_MODEL_PATH"

gazebo --verbose "$WORLD_DIR/worlds/terrain.world"
