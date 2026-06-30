# Generate a forest world
docker run -v $(pwd):/workspace forest3d generate

# Convert Blender assets to Gazebo models
docker run -v $(pwd):/workspace forest3d convert \
  -i /workspace/Blender-Assets -o /workspace/models -c tree

  docker run -v $(pwd):/workspace forest3d terrain \
  -d ./dem/enhanced_heightmap.tif


# Launch Gazebo to view the world (requires X11)
xhost +local:docker  # Allow Docker to access display
docker run -e DISPLAY=$DISPLAY \
           -v /tmp/.X11-unix:/tmp/.X11-unix \
           -v $(pwd):/workspace \
           --network host \
           forest3d launch