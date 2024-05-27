# Overview

This software is a Python application that uses the Pyglet library to render a 3D model and capture snapshots of the model at different angles as it rotates. The captured snapshots are saved as image files in a unique directory.

## Features

- **3D Model Loading:** Load and display a 3D model from a specified file path.
- **Initial Rotation:** Apply a random initial rotation to the model on the x-axis.
- **Lighting:** Configure ambient lighting for better visualization.
- **Rotation and Snapshot:** Rotate the model iteratively and capture snapshots of each rotated view, saving them to a directory.
- **Snapshot Directory:** Automatically create a unique directory based on the current date and time to store snapshots.

The script will perform the following steps:

1. Open a Pyglet window with a 3D view.
2. Load the specified 3D model.
3. Apply a random initial rotation to the model on the x-axis.
4. Set up ambient lighting.
5. Rotate the model around the y-axis iteratively.
6. Capture and save 30 snapshots of the model in different rotated views.
7. View the snapshots in the created directory. The directory will be named in the format Img/Img_YYYYMMDD_HHMMSS, where YYYYMMDD_HHMMSS is the current date and time.

## Configuration
You can configure the initial rotation angles, rotation speed, and axis of rotation by modifying the parameters in the script:

```
initial_rotation_x = random.randint(65, 115)
initial_rotation_y = 0
initial_rotation_z = 0
```
