import pyglet
from pyglet.gl import *
import random
from datetime import datetime
import os

class RotatingObject:
    def __init__(self, model_path, width=720, height=720, initial_rotation_x=0, initial_rotation_y=0, initial_rotation_z=0):
        self.window = pyglet.window.Window(width=width, height=height)
        self.window.projection = pyglet.window.Projection3D()
        self.batch = pyglet.graphics.Batch()
        self.snapshot_counter = 0

        # Initial rotations
        self.initial_rotation_x = initial_rotation_x
        self.initial_rotation_y = initial_rotation_y
        self.initial_rotation_z = initial_rotation_z

        # Create a unique directory to store images
        date_str = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.img_dir = f"Img/Img_{date_str}"
        os.makedirs(self.img_dir, exist_ok=True)

        # Load the model
        self.model = pyglet.model.load(model_path, batch=self.batch)

        # Apply initial rotation and translation
        # glTranslatef(0, 0, -0.35)
        glTranslatef(0, 0, random.uniform(-.35,-.75))

        self.apply_initial_rotation()

        # Configure ambient lighting
        self.setup_lighting()

        # Set up event handlers
        self.window.event(self.on_draw)

    def apply_initial_rotation(self):
        """Apply the initial rotations to the model."""
        glRotatef(self.initial_rotation_x, 1, 0, 0)
        glRotatef(self.initial_rotation_y, 0, 1, 0)
        glRotatef(self.initial_rotation_z, 0, 0, 1)

    def setup_lighting(self):
        """Set intense ambient light (R, G, B, A)."""
        # OpenGL settings
        glEnable(GL_MULTISAMPLE_ARB)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)

        ambient_light = (GLfloat * 4)(1.0, 1.0, 1.0, 1.0)
        glLightfv(GL_LIGHT0, GL_AMBIENT, ambient_light)

    def rotate(self, dt, angle, axis):
        """Rotate function for iterative rotation."""
        if axis == 'x':
            glRotatef(angle, 1, 0, 0)
        elif axis == 'y':
            glRotatef(angle, 0, 1, 0)
        elif axis == 'z':
            glRotatef(angle, 0, 0, 1)

    def on_draw(self):
        """Render the scene and capture a snapshot."""
        if self.snapshot_counter<=30:
            self.window.clear()
            self.batch.draw()
            filename = f"snapshot_{self.snapshot_counter}.jpg"
            full_path = os.path.join(self.img_dir, filename)
            pyglet.image.get_buffer_manager().get_color_buffer().save(full_path)
            print(f"Saved snapshot to {full_path}")
            self.snapshot_counter += 1
        else:
            pyglet.app.exit()


    def schedule_rotation(self, angle_increment, rotation_axis, interval=1 / 120):
        """Schedule the rotation for iterative views."""
        pyglet.clock.schedule_interval(lambda dt: self.rotate(dt, angle_increment, rotation_axis), interval)

    def run(self):
        """Start the pyglet application."""
        pyglet.app.run()


# Usage Example
if __name__ == '__main__':
    # pass
    initial_rotation_x = random.randint(65,115)
    initial_rotation_y = 0
    initial_rotation_z = 0
    print(initial_rotation_x)


    rotating_obj = RotatingObject(
        model_path="untitled.obj",
        initial_rotation_x=initial_rotation_x,
        initial_rotation_y=initial_rotation_y,
        initial_rotation_z=initial_rotation_z
    )
    rotating_obj.schedule_rotation(angle_increment=10, rotation_axis='y', interval=1 / 120)
    rotating_obj.run()
 