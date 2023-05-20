import numpy as np
from scipy.spatial import Voronoi

from main import *

# Image size
width = WIDTH
height = HEIGHT

# Set number of random seed points
num_points = 50

# Generate random seed points
points = np.random.rand(num_points, 2) * np.array([width, height])

# Generate Voronoi diagram based on seed points
vor = Voronoi(points)

# Create Image
image = generate_image(width=width, height=height, color=(255, 255, 255, 255))

# Draw each Voronoi cell with a random color
for region in vor.regions:
    if not -1 in region:
        polygon = [vor.vertices[i] for i in region]
        color = tuple(np.random.randint(0, 256, size=3)) + (255,)
        draw = ImageDraw.Draw(image)
        draw.polygon(polygon, fill=color)

# Save Image to a local file
save_image_to_file(image, '{}/{}/{}.png'.format(MEDIA_PATH, os.path.basename(os.path.abspath(__file__)).replace('.py', ''), datetime.now().strftime("%Y-%m-%d_%H-%M-%S")))
